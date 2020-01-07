#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker

# Create an engine for sqlite database
engine = db.create_engine('sqlite:///:memory:', echo=True)

# Base class to derive classes which are mapped 
# using the Declarative system 
Base = declarative_base()

class User(Base):

	__tablename__ = 'users'

	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

	name = Column(String(50))
	fullname = Column(String(50))
	nickname = Column(String(50))

	def __repr__(self):
		return "<User (name='%s', fullname='%s', nickname='%s')>" % (
				self.name, self.fullname, self.nickname
			)

Base.metadata.bind = engine 
Base.metadata.create_all()
# Session class serves as a factory for new Session objects.
# Ready to talk to the databse using the 'ORM handle' -> Session.
Session = sessionmaker() 
Session.configure(bind=engine) # once engine is available

if __name__ == '__main__':

	ed_user = User(name='ed', fullname='Ed Jones', nickname='Eddy')
	# Instantiate a session from sessionmaker which
	# is bound to the engine created.
	session = Session()
	session.add(ed_user)
	session.commit()
	# session.commit()
	# print(session.query(User).filter_by(name='ed').first())
	# # Query to find ed
	our_user = session.query(User).filter_by(name='ed').first()
	# for n, fn, nn in our_user:
	print(our_user.name, our_user.fullname, our_user.nickname)

