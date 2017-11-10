#!/usr/bin/python3

'''module: 5-fileter_cities
this module contains code that queries a MySQL db
'''

import sys
import MySQLdb

if __name__ == "__main__":

    # I know, I don't use these variables.  They're here for reference
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_DB_name = sys.argv[3]
    state_filter = sys.argv[4]

    # by default, host=localhost and port=3306
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    # select all cities and join name of state
    cur.execute("SELECT name\
                FROM cities\
                WHERE state_id =\
                (SELECT id FROM states\
                WHERE name = %s)\
                ORDER BY id;", (state_filter,))
    rows = cur.fetchall()

    first_pass = True
    for row in rows:
        if first_pass:
            print(row[0], end='')
            first_pass = False
        else:
            print(", {}".format(row[0]), end='')
    print()

    cur.close()
    db.close()
