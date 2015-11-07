import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Users(Base):
	__tablename__ = 'users'

	uid = Column(Integer, primary_key=True)
	email = Column(String(250), nullable=False)
	name = Column(String(250), nullable=False)


class Team(Base):
	__tablename__ = 'team'

	tid = Column(Integer, primary_key=True)
	team_name = Column(String(50), nullable=False)
	user_id = Column(Integer, ForeignKey('users.uid'))
	owner = relationship(Users)

	@property
	def serialize(self):
		return {
	   		'tid': self.tid,
        	'team name': self.team_name,
    	}

class Players(Base):
	__tablename__ = 'players'

	fname = Column(String(80), nullable=False)
	lname = Column(String(80), nullable=False)
	pid = Column(Integer, primary_key=True)
	number = Column(String(8))
	position = Column(String(20))
	team_id = Column(Integer, ForeignKey('team.tid'))
	team = relationship(Team)
	user_id = Column(Integer, ForeignKey('users.uid'))
	owner = relationship(Users)

	@property
	def serialize(self):
		return {
    		'pid': self.pid,
        	'number': self.number,
        	'first name': self.fname,
    		'last name': self.lname,
    		'position': self.position
		}

engine = create_engine('sqlite:///nhlteams.db')


Base.metadata.create_all(engine)