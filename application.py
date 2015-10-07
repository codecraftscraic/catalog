from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from final_app_database_setup import Base, Team, Users, Players

app  = Flask(__name__)

engine = create_engine('sqlite:///nhlteams.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

###TO DO: Remember edge case of empty roster or no teams, give option to create

#show all teams in database
@app.route('/')
@app.route('/teams/')
def showTeams():
	teamList = session.query(Team).all()
	return render_template('teams.html',teams=teamList)

#see the roster of a given team
@app.route('/teams/<int:team_id>/', methods=['GET','POST'])
@app.route('/teams/<int:team_id>/roster/', methods=['GET','POST'])
def showRoster(team_id):
	team=session.query(Team).filter(Team.tid == team_id).one()
	players=session.query(Players).filter(Players.team_id == team_id).all()
	return render_template('roster.html', team=team, players=players)

#edit the team name
@app.route('/teams/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeam(team_id):
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

#delete a team from the database
@app.route('/teams/<int:team_id>/delete/', methods=['GET', 'POST'])
def deleteTeam(team_id):
	deleteTeam=session.query(Team).filter(Team.tid == team_id).one()
	if request.method == 'POST':
		session.delete(deleteTeam.tid)
		session.commit()
		flash("Team deleted!")
		return redirect(url_for('showTeams'))
	else:
		return render_template('deleteTeam.html', team = deleteTeam)

@app.route('/teams/<int:team_id>/<int:pid>/edit/', methods=['GET', 'POST'])
def editPlayer(team_id,pid):
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
	if request.method == 'POST':
		if request.form['number'] and request.form['fname'] and request.form['lname'] and request.form['position']:
			newPlayer=Players(number=request.form['number'], fname=request.form['fname'],
							  lname=request.form['lname'], position=request.form['position'],
							  team_id=team_id)
			session.add(newPlayer)
			session.commit()
			return redirect(url_for('showRoster',team_id=team_id))
	return render_template('newPlayer.html', team_id = team_id)

@app.route('/teams/<int:team_id>/<int:pid>/delete/', methods=['GET', 'POST'])
def deletePlayer(team_id,pid):
	deletePlayer=session.query(Players).filter(Players.pid == pid).one()
	if request.method == 'POST':
		session.delete(deletePlayer)
		session.commit()
		return redirect(url_for('showRoster',team_id=team_id,pid=pid))
	else:
		return render_template('deletePlayer.html', players = deletePlayer)



if __name__ == '__main__':
	app.secret_key = 'secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
