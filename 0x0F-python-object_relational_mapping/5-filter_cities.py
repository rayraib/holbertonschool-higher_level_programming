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
    cs.execute("SELECT cities.name FROM cities\
                JOIN states ON\
                states.id = cities.state_id\
                WHERE states.name = (%s)\
                ORDER BY cities.id ASC", [name])
    rows = cs.fetchall()
    length = len(rows)
    if (length != 0):
        for idx, element in enumerate(rows):
            if idx == length - 1:
                print(element[0])
            else:
                print("{},".format(element[0]), end=" ")
    cs.close()
    db.close()
