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

#TODO finish changing this class over
class (Base):
	__tablename__ = ''

	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	description = Column(String(250))
	price = Column(String(8))
	course = Column(String(250))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurant.db')


Base.metadata.create_all(engine)