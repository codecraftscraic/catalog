from flask import Flask
app  = Flask(__name__)

@app.route('/')
@app.route('/teams')
def showTeams():
	team = session.query(Team).first()
	items = session.query(Players).filter_by(team_id = team.tid)
	output = ''
	for i in items:
		output += i.team_name
		output += '</br>'
	return output

@app.route('/teams/new')
def newTeam():
	return "New team"

@app.route('/teams/team_id/edit')
def editTeam():
	return "Edit teams"

@app.route('/teams/team_id/delete')
def deleteTeam():
	return "Delete teams"

@app.route('/teams/team_id')
@app.route('/teams/team_id/roster')
def showRoster():
	return "Rosters"

@app.route('/teams/team_id/roster/new')
def newPlayer():
	return "New player"

@app.route('/teams/team_id/roster/roster_id/edit')
def editPlayer():
	return "Edit player"

@app.route('/teams/team_id/roster/roster_id/delete')
def deletePlayer():
	return "Delete player"

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












