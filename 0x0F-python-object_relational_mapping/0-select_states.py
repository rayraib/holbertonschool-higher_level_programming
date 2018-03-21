#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa:
'''
import MySQLdb
import sys
db = MySQLdb.connect(
    host='localhost',
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    )
'''
    use cursor to make queries
'''
cursor = db.cursor()
cursor.execute('USE hbtn_0e_0_usa')
cursor.execute('SELECT * FROM states')
results = cursor.fetchall()
for row in results:
    print (row)
