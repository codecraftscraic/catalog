from flask import Flask, render_template, url_for, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from final_app_database_setup import Base, Team, Users, Players

app  = Flask(__name__)

engine = create_engine('sqlite:///nhlteams.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

###TO DO: Remember edge case of empty roster or no teams, give option to create

@app.route('/')
@app.route('/teams/')
def showTeams():
	#return "All teams"
	team = session.query(Team).all()
	return render_template('teams.html', Team = team)

@app.route('/teams/<int:tid>/new', methods=['GET', 'POST'])
def newTeam(tid):
	#return "New team"
	return render_template('templates/newTeam.html', Team = team)

@app.route('/teams/<int:tid>/edit/', methods=['GET', 'POST'])
def editTeam(tid):
	#return "Edit teams"
	return render_template('templates/editTeam.html', Team = team)

@app.route('/teams/<int:tid>/delete/', methods=['GET', 'POST'])
def deleteTeam(tid):
	#return "Delete teams"
	return render_template('templates/deleteTeam.html', Team = team)

@app.route('/teams/<int:tid>/')
@app.route('/teams/<int:tid>/roster/')
def showRoster(tid):
	#return "Rosters"
	return render_template('templates/roster.html', Team = team, Players = player)

@app.route('/teams/<int:tid>/<int:pid>/new/', methods=['GET', 'POST'])
def newPlayer(pid):
	#return "New player"
	return render_template('templates/newPlayer.html', Team = team, Players = player)

@app.route('/teams/<int:tid>/<int:pid>/edit/', methods=['GET', 'POST'])
def editPlayer(pid):
	#return "Edit player"
	return render_template('templates/editPlayer.html', Team = team, Players = player)

@app.route('/teams/<int:tid>/<int:pid>/delete/', methods=['GET', 'POST'])
def deletePlayer(pid):
	#return "Delete player"
	return render_template('templates/deletePlayer.html', Team = team, Players = player)













if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)