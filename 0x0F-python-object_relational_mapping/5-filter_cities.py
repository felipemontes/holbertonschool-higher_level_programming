#!/usr/bin/python3
'''
script that takes in the name of a state as an argument and lists all cities
'''
import MySQLdb
import sys


def mysqlconnect():

    db_connection = None
    db_connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3], port=3306)
    cursor = db_connection.cursor()

    cursor.execute("SELECT cities.name FROM cities INNER JOIN"
                   " states ON cities.state_id = states.id WHERE"
                   " states.name= %s", (sys.argv[4],))

    states = cursor.fetchall()

    print(", ".join([state[0] for state in states]))

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
