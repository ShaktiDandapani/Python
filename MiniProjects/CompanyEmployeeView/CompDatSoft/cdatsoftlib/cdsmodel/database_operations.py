#!/usr/bin/env python
#-*- coding: utf-8 -*-
from database_model import Users

def create_user(session, first_name, last_name,	address, 
		university, degree, role, salary, birth_date, 
		join_date, email_id):
	
	new_user = Users(first_name=first_name, last_name=last_name,
			 address=address, university=university, degree=degree,
			 role=role, salary=salary, birth_date=birth_date,
			 join_date=join_date, email_id=email_id)
	session.add(new_user)

	return session