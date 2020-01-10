#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sqlalchemy as db 
from sqlalchemy.orm import sessionmaker
# import database_model as dbm
from database_model import Users, Base
import database_operations as dbops
import os 


class DBConn():

	def __init__(self, db_path):
		self.db_path = db_path
		self.sql_db  = 'sqlite:///'+self.db_path

	def create_database(self):
		# if not os.path.exists(db_path):
		engine = db.create_engine(self.sql_db)
		engine.echo = False
		Base.metadata.create_all(engine)
		metadata = db.MetaData(engine)
		DBSession = sessionmaker(bind=engine, autoflush=False)
		self.session = DBSession()

		self.session = dbops.create_user(
			self.session, 
			first_name='Shakti', 
			last_name='Dandapani',
			address='India', 
			university='Sheffield', 
			degree='Computer Science',
			role='Student',
		        salary=100,
			birth_date='02-09-1991-',
			join_date='01-02-2020',
		        email_id='shaktidhar_dandapani@gmail.com')
		
		self.session.commit()
		# print(session.query(Users).all())

		return self.session

	def load_database(self):
		session = None


		return self.session

	def get_session(self):

		return self.session

if __name__ == '__main__':
	db_path = '../../data/cdatsoftdb.db'
	
	# if os.path.exists(db_path):
	# 	session = load_database(db_path)
	# else:
	dbconn = DBConn(db_path)
	session = dbconn.create_database()
	print("Hi")
	# Commit after all steps are done
	# Might want to shift to controller folder


