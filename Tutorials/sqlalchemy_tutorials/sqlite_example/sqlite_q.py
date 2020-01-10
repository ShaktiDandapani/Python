#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

Script to query database items.
('example.db')

"""

import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()
c.execute('SELECT * FROM person')
print(c.fetchall())
c.execute('SELECT * FROM address')
print(c.fetchall())
conn.close()