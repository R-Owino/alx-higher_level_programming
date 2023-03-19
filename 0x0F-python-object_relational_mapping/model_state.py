#!/usr/bin/python3

"""
Contains the class definition of a State and an instance Base
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine


# instance of declarative_base
Base = declarative_base()


# state class
class State(Base):
    """
    Defines a class state that represents a table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


# connect to MySQL server running on localhost at port 3306
engine = create_engine('mysql://localhost:3306/hbtn_0e_6_usa?charset=utf8',
                       / echo=True)
Base.metadata.create_all(engine)
