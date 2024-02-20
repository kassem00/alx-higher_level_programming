#!/usr/bin/python3
"""
script that lists all states name start with N
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    query = "SELECT name FROM cities WHERE state_id=(SELECT id FROM\
    states WHERE name=%s LIMIT 1)"
    c.execute(query, (sys.argv[4],))

    cities = [city[0] for city in c.fetchall()]
    print(", ".join(cities))

    c.close()
    db.close()
