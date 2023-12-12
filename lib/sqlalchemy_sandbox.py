#!/usr/bin/env python3
# lib/sqlalchemy_sandbox.py
# Schema - this is the blueprint of a database ie describes how data related to other data in tables
#           columns, and relatonships between them 

# Persisit - save schema to a database 

# Engine - a python object that translates SQL to PYTHON and vice versa 

# Session - a Python object that uses an engine to allow us to programmatically
#           interact with a database 

# Transaction - a strategy for executing database statements such that the group
#               suceeds or fails as a unit 

# Migration - the process of moving data from one or more databases to one or more target databases



from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base): # Inheritance from a declarative_base object.

    __tablename__ = 'students' # A __tablename__ class attribute which will be used as the name of our SQL database

    # One or more Columns as class attributes
    id = Column(Integer(), primary_key=True) # A Column specified to be the table's primary key
    name = Column(String())
    breed = Column(String())

# this persists our schema to the database 
if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)