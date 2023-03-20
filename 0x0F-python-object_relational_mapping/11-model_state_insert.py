#!/usr/bin/python3

"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    # create engine that connects to the database
    engine = create_engine(f'''mysql+mysqldb://{username}:{password}@localhost:
            3306/{database}''')

    # create tables in the database if they don't exist already
    Base.metadata.create_all(engine)

    # create a session factory
    Session = sessionmaker(bind=engine)

    # create session object
    session = Session()

    # Add new state object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # print id of the new state
    print(new_state.id)

    # close session
    session.close()
