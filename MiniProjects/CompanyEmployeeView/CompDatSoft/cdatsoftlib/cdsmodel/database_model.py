#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
	__tablename__ = 'Users'
	id = Column(Integer, primary_key=True)
	name = Column(String(40))
	address = Column(String(40))
	university = Column(String(40))
	# degree = Column(String(40))
	role = Column(String(40))

	def __repr__(self):

		return "< User Name: {}, Address: {}, University: {} >".format(self.name,
			self.address, self.university)