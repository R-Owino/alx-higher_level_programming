#!/usr/bin/python3

"""
Contains the class definition of a State and an of instance Base
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from relationship_city import Base, City


# state class
class State(Base):
    """
    Defines a class state that represents a table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete",
                          backref=backref("state"))
