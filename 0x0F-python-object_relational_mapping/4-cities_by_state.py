#!/usr/bin/python3

'''module: 4-cities_by_state
this module contains code that queries a MySQL db
'''

import sys
import MySQLdb

if __name__ == "__main__":

    # I know, I don't use these variables.  They're here for reference
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_DB_name = sys.argv[3]

    # by default, host=localhost and port=3306
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    # select all cities and join name of state
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
