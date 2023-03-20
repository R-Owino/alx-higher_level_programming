#!/usr/bin/python3

"""
prints the State object with the name passed as argument from the database
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Getting username, password and database name from commandline args
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # create enginne that connects to the database
    engine = create_engine(f'''mysql+mysqldb://{username}:{password}@localhost:
            3306/{database}''')

    # Create tables in the database if they don't exist
    Base.metadata.create_all(engine)

    # create a configured session class
    Session = sessionmaker(bind=engine)

    # create a Session instance
    session = Session()

    # query database to get all city objects
    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])

    # close session
    session.close()
