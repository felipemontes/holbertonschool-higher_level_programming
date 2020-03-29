#!/usr/bin/python3
'''
script that takes in an argument and displays all values in the states
'''
import MySQLdb
import sys


def mysqlconnect():

    db_connection = None
    db_connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3], port=3306)
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE '{}' "
                   "COLLATE Latin1_General_CS;".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
