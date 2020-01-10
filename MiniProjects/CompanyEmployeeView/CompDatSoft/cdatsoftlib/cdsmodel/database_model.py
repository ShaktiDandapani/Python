#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
	__tablename__ = 'Users'
	id = Column(Integer, primary_key=True)
	first_name = Column(String(40))
	last_name = Column(String(40))
	address = Column(String(40))
	university = Column(String(40))
	degree = Column(String(40))
	role = Column(String(40))
	salary = Column(Integer)
	birth_date = Column((String(10)))
	join_date = Column((String(10)))
	email_id = Column(String(100))

	def __repr__(self):

		return "< User Name: {}, Address: {}, University: {} >".format(self.first_name,
			self.address, self.university)


class Employee(Base):
	__tablename__ = 'Employee'
	emp_id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey(Users.id))
	email_id = Column(String(100), ForeignKey(Users.email_id))
	user_name = Column(String(20))
	password = Column(String(20))
	
	
	def __repr__(self):
		return "<User Name: {}>".format(self.user_name)
	