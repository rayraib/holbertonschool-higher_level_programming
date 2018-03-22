#!/usr/bin/python3
'''
    script that lists all City objects from the database hbtn_0e_101_usa
'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City, Base
from relationship_state import State
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    # Create engine that opens connection between the class state and
    # the database with the data
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (uname, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    #
    for state in session.query(State).all():
        state_name = state.name
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state_name))
    session.close()
