#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine, select)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    connection = engine.connect()
    s = select([State])
    rp = connection.execute(s)
    results = rp.fetchall()

    for row in sorted(results, key=lambda tup: tup[0]):
        print("{}: {}".format(row[0], row[1]))
