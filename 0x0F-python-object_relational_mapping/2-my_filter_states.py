#!/usr/bin/python3

'''module: 2-my_filter_states
this module contains code that connect to a MySQL db and filters a query
'''

import sys
import MySQLdb

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_DB_name = sys.argv[3]
    my_filter = sys.argv[4]

    # by default, host=localhost and port=3306
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states\
                WHERE name = '{}'".format(my_filter))
    rows = sorted(cur.fetchall(), key=lambda tup: tup[0])

    # print all states that start with letter N
    for row in rows:
        print(row)

    cur.close()
    db.close()
