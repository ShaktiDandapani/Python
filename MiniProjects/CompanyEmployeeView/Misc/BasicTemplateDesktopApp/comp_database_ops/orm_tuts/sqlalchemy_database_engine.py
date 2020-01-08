#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')


with engine.connect() as con:

	rs = con.execute('SELECT 5')
	data = rs.fetchone()[0]

	print("Data: %s" % data)