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
    query = ("SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
             .format(state))
    cs = db.cursor()
    cs.execute(query)
    rows = cs.fetchall()
    if len(rows) != 0:
        for row in rows:
            if row[1] == state:
                print(row)
    cs.close()
    db.close()
