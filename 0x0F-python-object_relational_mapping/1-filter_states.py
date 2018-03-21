#!/usr/bin/python3
'''
    a script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa:
'''
import MySQLdb
import sys

db = MySQLdb.connect(
    host='localhost',
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
    )
cs = db.cursor()
cs.execute('USE hbtn_0e_0_usa')
cs.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id ASC')
rows = cs.fetchall()
for row in rows:
    print(row)
