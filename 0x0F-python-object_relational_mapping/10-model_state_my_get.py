#!/usr/bin/python3

"""
prints State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    # Getting username, password and database name from commandline args
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    # create the engine that connects to the database
    engine = create_engine(f'''mysql+mysqldb://{username}:{password}@localhost:
            3306/{database}''')

    # create tables in the database if they don't exist already
    Base.metadata.create_all(engine)

    # create a session factory
    Session = sessionmaker(bind=engine)

    # create session object
    session = Session()

    # query database for the state object name passed as argument
    state = session.query(State).filter(State.name == state_name).first()

    # print the state
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # close session
    session.close()
