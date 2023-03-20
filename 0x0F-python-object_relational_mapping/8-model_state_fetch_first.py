#!/usr/bin/python3

"""
script that prints the first State object from the database hbtn_0e_6_usa
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

    """Connect to MySQL server running on localhost at port 3306
    and select the database"""
    engine = create_engine(f'''mysql+mysqldb://{username}:{password}@localhost:
            3306/{database}''')

    # create tables in the database if they don't exist already
    Base.metadata.create_all(engine)

    # create a session factory
    Session = sessionmaker(bind=engine)

    # create session object
    session = Session()

    # query database to get the first state object
    state = session.query(State).first()

    # print the state
    if state is None:
        print("Nothing")
    else:
        print(state.id, state.name, sep=": ")

    # close session
    session.close()
