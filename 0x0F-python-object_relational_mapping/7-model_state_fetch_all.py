#!/usr/bin/python3
'''
script that lists all State objects from the database
'''
from sqlalchemy import Column, Integer, String, create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    for row in query.all():
        print("{}: {}".format(row.id, row.name))
