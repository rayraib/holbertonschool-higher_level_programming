#!/usr/bin/python3
'''
    a script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
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
    state = sys.argv[4]
    cs = db.cursor()
    cs.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
               (state,))
    rows = cs.fetchall()
    if len(rows) != 0:
        for row in rows:
            print(row)
    db.close()
