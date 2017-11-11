#!/usr/bin/python3
"""Module: 11-model_state_instert
Links class to table in database, then fetches filtered query
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, select)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    connection = engine.connect()
    Session = sessionmaker(bind=engine)

    session = Session()
    new_state = State(name="Louisiana")

    session.add(new_state)
    # commit the record the database
    session.commit()

    query = session.query(State).filter(State.name == 'Louisiana').first()

    if query is None:
        print("Timbuktoo")
    else:
        print(query.id)
