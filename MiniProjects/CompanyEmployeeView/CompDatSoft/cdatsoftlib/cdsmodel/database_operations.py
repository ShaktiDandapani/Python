#!/usr/bin/env python
#-*- coding: utf-8 -*-
from database_model import Users

def create_user(session, name, address, university, role):
	
	new_user = Users(name=name, address=address, university=university, role=role)
	session.add(new_user)

	return session