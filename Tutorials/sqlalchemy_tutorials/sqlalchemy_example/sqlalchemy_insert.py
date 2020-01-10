#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Address, Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db')
engine.echo = True
# Bind the engine to the metadata of the Base class, 
# so that the declaratives can be accessed through 
# a DBSession interface 

Base.metadata.bind = engine 

DBSession = sessionmaker(bind=engine)

session = DBSession()

# insert a new Person
new_person = Person(name='new person')
session.add(new_person)
session.commit()

# Insert a new address 
new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()