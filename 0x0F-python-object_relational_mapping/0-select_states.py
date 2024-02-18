#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
arg = sys.argv

if __name__ == "__main__":
    db=_mysql.connect("localhost", arg[1], arg[2], arg[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
