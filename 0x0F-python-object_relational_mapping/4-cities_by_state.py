#!/usr/bin/python3
'''
script that lists all cities from the database
'''
import MySQLdb
import sys


def mysqlconnect():

    db_connection = None
    db_connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3], port=3306)
    cursor = db_connection.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM"
                   " cities INNER JOIN states ON cities.state_id = states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
