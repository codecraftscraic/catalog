from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from final_app_database_setup import Base, Team, Users, Players
from flask import session as login_session 
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response

import random, string
import httplib2
import json
import requests

app  = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json','r').read())['web']['client_id']
APPLICATION_NAME = "Hockey Catalog"

engine = create_engine('sqlite:///nhlteams.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

###TO DO: Remember edge case of empty roster or no teams, give option to create

#Create state token for anti-forgery
@app.route('/login')
def showLogin():
		state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
		login_session['state'] = state
		return render_template('login.html', STATE=state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Auth code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access session token
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    #check if return user
    user_id = getUserID(login_session['email'])
    if not user_id:
    	user_id = createUser(login_session)
    login_session['user_id'] = users.uid

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

#Logout
@app.route('/gdisconnect')
def gdisconnect():
	credentials = login_session.get('credentials')
	if credentials is None:
		response = make_response(json.dumps('Current user not connected.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	access_token = credentials
	url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
	h = httplib2.Http()
	result = h.request(url, 'GET')[0]

	if result['status'] == '200':
		#reset user info
		del login_session['credentials']
		del login_session['gplus_id']
		del login_session['username']
		del login_session['email']
		del login_session['picture']

		response = make_response(json.dumps('Successfully disconnected.'), 200)
		response.headers['Content-Type'] = 'application/json'
		#return render_template('teams.html')
		return response
	else:
		response = make_response(json.dumps('Failed to logout user.'), 400)
		response.headers['Content-Type'] = 'application.json'
		return response

#show all teams in database
@app.route('/')
@app.route('/teams/')
def showTeams():
	teamList = session.query(Team).all()
	if 'username' not in login_session:
		flash('Please login to make changes.')
		return render_template('public_teams.html',teams=teamList)
	else:
		return render_template('teams.html',teams=teamList)

#see the roster of a given team
@app.route('/teams/<int:team_id>/', methods=['GET','POST'])
@app.route('/teams/<int:team_id>/roster/', methods=['GET','POST'])
def showRoster(team_id):
	team=session.query(Team).filter(Team.tid == team_id).one()
	players=session.query(Players).filter(Players.team_id == team_id).all()
	if 'username' not in login_session:
		flash('Please login to make changes.')
		return render_template('public_roster.html', team=team, players=players)
	else:
		return render_template('roster.html', team=team, players=players)

#edit the team name
@app.route('/teams/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeam(team_id):
	if 'username' not in login_session:
		return redirect('/login')

	team_owner=session.query(Team).filter(Team.tid == team_id).one()
	owner=getUserInfo(team_owner.user_id)

	if owner.name != login_session['username']:
		flash('You are not the owner of this team, and cannot edit it.')
	else: 
		editedTeam=session.query(Team).filter(Team.tid == team_id).one()
		if request.method == 'POST':
			if request.form['teamname']:
				editedTeam.team_name = request.form['teamname']
				session.add(editedTeam)
				session.commit()
				flash("Team updated!")
			return redirect(url_for('showTeams'))
		else:
			return render_template('editTeam.html', team = editedTeam)

@app.route('/teams/<int:team_id>/<int:pid>/edit/', methods=['GET', 'POST'])
def editPlayer(team_id,pid):
	if 'username' not in login_session:
		return redirect('/login')

	player_owner=session.query(Players).filter(Players.pid == pid).one()
	owner=getUserInfo(player_owner.user_id)

	if owner.name != login_session['username']:
		flash('You are not the owner of this team, and cannot edit it.')
	else:
		editedPlayer=session.query(Players).filter(Players.pid == pid).one()
		if request.method == 'POST':
			if request.form['number']:
				editedPlayer.number = request.form['number']
				session.add(editedPlayer)
				session.commit()
				flash("Player number updated!")
			if request.form['fname']:
				editedPlayer.fname = request.form['fname']
				session.add(editedPlayer)
				session.commit()
				flash("Player's first name updated!")
			if request.form['lname']:
				editedPlayer.lname = request.form['lname']
				session.add(editedPlayer)
				session.commit()
				flash("Player last name updated!")
			if request.form['position']:
				editedPlayer.position = request.form['position']
				session.add(editedPlayer)
				session.commit()
				flash("Player position updated!")
				#TO DO Ask if done editing the player before rendering the home page
			return redirect(url_for('showRoster',team_id=team_id,pid=pid))
		else:
			return render_template('editPlayer.html', players = editedPlayer)

@app.route('/teams/<int:team_id>/newplayer/', methods=['GET', 'POST'])
def newPlayer(team_id):
	if 'username' not in login_session:
		return redirect('/login')

	if request.method == 'POST':
		if request.form['number'] and request.form['fname'] and request.form['lname'] and request.form['position']:
			newPlayer=Players(number=request.form['number'], fname=request.form['fname'],
							  lname=request.form['lname'], position=request.form['position'],
							  team_id=team_id, user_id=login_session['user_id'])
			session.add(newPlayer)
			session.commit()
			return redirect(url_for('showRoster',team_id=team_id))
	return render_template('newPlayer.html', team_id = team_id)

@app.route('/teams/<int:team_id>/<int:pid>/delete/', methods=['GET', 'POST'])
def deletePlayer(team_id,pid):
	if 'username' not in login_session:
		return redirect('/login')

	deletePlayer=session.query(Players).filter(Players.pid == pid).one()
	if request.method == 'POST':
		session.delete(deletePlayer)
		session.commit()
		return redirect(url_for('showRoster',team_id=team_id,pid=pid))
	else:
		return render_template('deletePlayer.html', players = deletePlayer)

def getUserID(email):
	try:
		user = session.query(Users).filter_by(email = email).one()
		return user.uid
	except:
		return None

def getUserInfo(user_id):
	user = session.query(Users).filter_by(uid = user_id).one()
	return user

def createUser(login_session):
	newUser = Users(name = login_session['username'], email = login_session['email'])
	session.add(newUser)
	session.commit()
	user = session.query(Users).filter_by(email = login_session['email']).one()
	return user.uid


if __name__ == '__main__':
	app.secret_key = 'secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
