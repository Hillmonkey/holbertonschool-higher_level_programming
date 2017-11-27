#!/usr/bin/python3
"""Module: 8-model_state_fetch_first
Links class to table in database, then fetches filtered query
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, select)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    my_filter = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    connection = engine.connect()
    Session = sessionmaker(bind=engine)

    session = Session()
    results = session.query(State).filter(State.name == my_filter).first()

    if results is None:
        print("Not found")
    else:
        print(results.id)
