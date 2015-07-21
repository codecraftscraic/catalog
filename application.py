from flask import Flask, url_for
app  = Flask(__name__)

###TO DO: Remember edge case of empty roster or no teams, give option to create

@app.route('/')
@app.route('/teams/')
def showTeams():
	#return "All teams"
	session.query.all()
	return render_template('templates/teams.html', team = team)

@app.route('/teams/new')
def newTeam(tid):
	#return "New team"
	return render_template('templates/newTeam.html', team = team)

@app.route('/teams/<int:tid>/edit/')
def editTeam(tid):
	#return "Edit teams"
	return render_template('templates/editTeam.html', team = team)

@app.route('/teams/<int:tid>/delete/')
def deleteTeam(tid):
	#return "Delete teams"
	return render_template('templates/deleteTeam.html', team = team)

@app.route('/teams/<int:tid>/')
@app.route('/teams/<int:tid>/roster/')
def showRoster(tid):
	#return "Rosters"
	return render_template('templates/roster.html', team = team, player = player)

@app.route('/teams/<int:tid>/roster/new/')
def newPlayer(pid):
	#return "New player"
	return render_template('templates/newPlayer.html', team = team, player = player)

@app.route('/teams/<int:tid>/roster/<int:pid>/edit/')
def editPlayer(pid):
	#return "Edit player"
	return render_template('templates/editPlayer.html', team = team, player = player)

@app.route('/teams/<int:tid>/roster/<int:pid>/delete/')
def deletePlayer(pid):
	#return "Delete player"
	return render_template('templates/deletePlayer.html', team = team, player = player)

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from final_app_database_setup.py import Base, Teams, Users, Players

engine = create_engine('sqlite:///nhlteams.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()












