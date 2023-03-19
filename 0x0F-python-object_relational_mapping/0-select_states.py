#!/usr/bin/python3

"""
script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Getting username, password and database name from commandline args
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # connect to MySQL server running on lovalhost at port 3306
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            password=password, database=database)

    # cursor object
    cursor = db.cursor()

    # SQL query to fetch all states from states table
    cursor.execute("SELECT * FROM states ORDER BY id")

    # fetch all rows
    rows = cursor.fetchall()

    # print the states
    for row in rows:
        print(row)

    # close cursor and database connections
    cursor.close()
    db.close()
