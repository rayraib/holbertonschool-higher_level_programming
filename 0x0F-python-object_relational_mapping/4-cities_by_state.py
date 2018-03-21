#!/usr/bin/python3
'''
    a script that lists all cities from the database hbtn_0e_e_usa
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
    cs = db.cursor()
    cs.execute('SELECT * FROM cities ORDER BY id ASC')
    rows = cs.fetchall()
    for row in rows:
        print(row)
    db.close()
