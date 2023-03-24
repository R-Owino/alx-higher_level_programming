#!/usr/bin/python3

"""
lists all State objects and corresponding City objects contained
in the database hbtn_0e_101_usa

"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    # Getting username, password and database name from commandline args
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # create engine that connects to the database
    engine = create_engine(f'''mysql+mysqldb://{username}:{password}@localhost:
            3306/{database}''', pool_pre_ping=True)

    # create tables in the database if they don't exist already
    Base.metadata.create_all(engine)

    # craete a configured class session
    Session = sessionmaker(bind=engine)

    # create a Session instance
    session = Session()

    # Query all City objects with related State object
    for state in session.query(State).order_by(State.id):
        for city_obj in state.cities:
            print(city_obj.id, city_obj.name, sep=": ", end="")
            print(" -> " + state.name)
