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


if __name__ == "__main__":
    # Getting username, password and database name from commandline args
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # create enginne that connects to the database
    engine = create_engine(f'''mysql+mysqldb://{username}:{password}@localhost:
            3306/{database}''', pool_pre_ping=True)

    # create tables in the database if they don't exist already
    Base.metadata.create_all(engine)

    # create a configured session class
    Session = sessionmaker(bind=engine)

    # create a Session instance
    session = Session()

    # create and add new state and city objects
    new_state = State(name='Carlifornia')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add_all([new_city, new_state])
    session.commit()

    # close session
    session.close()
