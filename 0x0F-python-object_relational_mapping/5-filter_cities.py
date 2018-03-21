#!/usr/bin/python3
'''
    script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    name = sys.argv[4]
    cs = db.cursor()
    cs.execute('SELECT cities.name FROM states, cities\
                WHERE states.id = state_id and states.name = %s\
                ORDER BY states.id ASC', (name,))
    rows = cs.fetchall()
    length = len(rows)
    if length != 0:
        for idx, row in enumerate(rows):
            if idx != length - 1:
                print("{}".format(row[0]), end=", ")
            else:
                print("{}".format(row[0]))
    db.close()
