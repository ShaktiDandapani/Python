#/usr/bin/env python
#-*- coding: utf-8 -*-

"""

Query from the sqlalchemy_example.db.

"""

from sqlalchemy_declarative import Person, Base, Address
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')
engine.echo = True
Base.metadata.bind = engine 

DBSession = sessionmaker()
session = DBSession()

q_person_all = session.query(Person).all()

print(q_person_all)

person = session.query(Person).first()

print(person.name)

# Find all Addresses whose person field is pointing to the person object
q_per_address = session.query(Address).filter(Address.person == person).all()
print(q_per_address)

# Find only one address whose person field is pointing to the person object
q_per_address_one = session.query(Address).filter(Address.person == person).one()
print(q_per_address_one)

address = session.query(Address).filter(Address.person == person).one()
print(address.post_code)




