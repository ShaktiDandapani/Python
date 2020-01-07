#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

Tutorial from:
http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html

"""

import sqlalchemy as db 
from sqlalchemy import Integer, String, Column

engine = db.create_engine('sqlite:///tutorial.db')

engine.echo = True

metadata = db.MetaData(engine)

# if users database exists:
# 	users = Table('users', metadata, autoload=True)
# else:

users = db.Table('users', metadata,
			Column('user_id', Integer, primary_key=True),
			Column('name', String(40)),
			Column('age', Integer),
			Column('password', String),
		)

users.create()

_ins = users.insert()
_ins.execute(name='Mary', age=30, password='secret')
_ins.execute({'name': 'John', 'age': 42},
			 {'name': 'Susan', 'age': 57},
			 {'name': 'Carl', 'age': 33})

_sel = users.select()
_rs = _sel.execute()

row = _rs.fetchone()

print('Id: ', row[0])
print('Name: ', row['name'])
print('Age: ', row.age)
print('Password: ', row[users.c.password])

for row in _rs:
	print(row.name, 'is ', row.age, 'years old')