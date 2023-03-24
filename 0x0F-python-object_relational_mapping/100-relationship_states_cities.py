#!/usr/bin/python3

"""
script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # getting username, password and database name from commandline args
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # create engine taht connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # create tables in the database if they don't exist already
    Base.metadata.create_all(engine)

    # create configured session class and session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # create and add bew state and city objects
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()
