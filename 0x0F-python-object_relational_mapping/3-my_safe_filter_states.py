#!/usr/bin/python3
'''
Fixing Mysql injection
'''
import MySQLdb
import sys


def mysqlconnect():

    db_connection = None
    db_connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3], port=3306)
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name= %s", (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
