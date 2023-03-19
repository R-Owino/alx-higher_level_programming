#!/usr/bin/python3


"""
script that takes in an argument and displays all values in states table
of hbtn_0e_0_usa where name matches the argument, safe from SQL injection
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Getting username, password and database name from commandline args
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    # connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=database)

    # cursor object
    cursor = db.cursor()

    # SQL query to fetch all states with given name
    query = """SELECT * FROM states
            WHERE name LIKE %s
            ORDER BY id"""
    cursor.execute(query, (state_name,))

    # fetch all rows
    rows = cursor.fetchall()

    # print the states
    for row in rows:
        print(row)

    # close cursor and database connections
    cursor.close()
    db.close()
