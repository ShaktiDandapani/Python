#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

Code from:
https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/

Script creating two tables, 
1. Person. 
2. Address.

"""
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''
          CREATE TABLE person
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          '''
          )
c.execute('''
          CREATE TABLE address
          (id PRIMARY KEY ASC, street_name varchar(25), street_number varchar(250),
          post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
          FOREIGN KEY(person_id) REFERENCES person(id))
          '''
          )

c.execute('''
          INSERT INTO person VALUES(1, 'pythoncentral')
          '''
          )

c.execute('''
          INSERT INTO address VALUES(1, 'pytihon road', '1', '00000', 1)
          '''
          )

conn.commit()
conn.close()