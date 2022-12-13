import math
import mysql.connector

def doQuery(query):
    cursor.execute(query)
    res = cursor.fetchall()
    for row in res:
     print(row)

def main():
    pass
main()