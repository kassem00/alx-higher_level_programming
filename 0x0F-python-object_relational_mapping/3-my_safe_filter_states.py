#!/usr/bin/python3
"""
script that lists all states name start with N
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
arg = sys.argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("\
    SELECT\
    *\
    FROM\
    `states`")
    for state in c.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
