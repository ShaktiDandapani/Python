#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sqlalchemy as db 
from sqlalchemy import and_, or_, not_

engine = db.create_engine('sqlite:///tutorial.db')

engine.echo = True 

metadata = db.MetaData(engine)

# The table already exists, 
# therefore we load it from the existing db file.
users = db.Table('users', metadata, autoload=True)

def run(stmt):
	_rs = stmt.execute()
	for row in _rs:
		print(row)

# Select users with the name john
_sel = users.select(users.c.name == 'John')
run(_sel)
_sel = users.select(users.c.age < 40)
run(_sel)

# More statements
_sel = users.select(and_(users.c.age < 40, users.c.name != 'Mary'))
run(_sel)
_sel = users.select(or_(users.c.age < 40, users.c.name != 'Mary'))
run(_sel)
_sel = users.select(not_(users.c.name == 'Susan'))

# Substitutes for and or not, but be aware of priority
_sel = users.select((users.c.age < 40) & (users.c.name != 'Mary'))
run(_sel)
_sel = users.select((users.c.age < 40) | (users.c.name != 'Mary'))
run(_sel)
_sel = users.select(~(users.c.name == 'Susan'))
run(_sel)

# Like, Startswith, Endswith
_sel = users.select(users.c.name.startswith('M'))
run(_sel)
_sel = users.select(users.c.name.like('%a%'))
run(_sel)
_sel = users.select(users.c.name.endswith('n'))
run(_sel)

# In and between operations
_sel = users.select(users.c.age.between(30, 39))
run(_sel)
_sel = users.select(users.c.name.in_(('Mary', 'Susan')))
run(_sel)

# Calling SQL functions
