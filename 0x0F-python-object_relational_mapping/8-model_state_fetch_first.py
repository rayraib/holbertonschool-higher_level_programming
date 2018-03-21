#!/usr/bin/python3
'''
    Script that prints the first State object from the database hbtn_0e_6_usa
'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import State, Base
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]

    #Create engine that opens connection between the class state and
    # the database with the data
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                          (uname, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    #create session
    Session = sessionmaker(bind=engine)
    session = Session()

    #query the database
    first = session.query(State)
    if first is not None:
        print("{}: {}".format(first[0].id, first[0].name))
    else:
        print("Nothing")
