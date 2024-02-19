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

    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    try:
        search = sys.argv[4] + " " + sys.argv[5]
    except IndexError:
        search = sys.argv[4]
    print(search)
    for city in c.fetchall():
        if search in city:
            print(city)
