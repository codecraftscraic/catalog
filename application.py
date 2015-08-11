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
			editTeam.name = request.form['teamname']
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
	return render_template('deleteTeam.html', team = deleteTeam)

#@app.route('/teams/<int:team_id>/new', methods=['GET', 'POST'])
#def newTeam(team_id):
	#return "New team"
#	return render_template('newTeam.html', Team = team)

#@app.route('/teams/<int:team_id>/<int:pid>/new/', methods=['GET', 'POST'])
#def newPlayer(pid):
	#return "New player"
#	return render_template('newPlayer.html', Team = team, Players = player)

#@app.route('/teams/<int:team_id>/<int:pid>/edit/', methods=['GET', 'POST'])
#def editPlayer(pid):
	#return "Edit player"
#	return render_template('editPlayer.html', Team = team, Players = player)

#@app.route('/teams/<int:team_id>/<int:pid>/delete/', methods=['GET', 'POST'])
#def deletePlayer(pid):
	#return "Delete player"
#	return render_template('deletePlayer.html', Team = team, Players = player)



if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)