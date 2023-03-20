#!/usr/bin/python3

"""
Contains the class definition of a State and an instance Base
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData


# instance of declarative_base
meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


# state class
class State(Base):
    """
    Defines a class state that represents a table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
