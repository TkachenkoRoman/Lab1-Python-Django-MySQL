#!/usr/bin/env python
import os
import sys
import MySQLdb

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Lab1.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)



""" cursor.execute('SELECT * FROM guitar_types;')
results = cursor.fetchall()
for row in results:
    print row

cursor.execute('SELECT * FROM Produser;')
results = cursor.fetchall()
for row in results:
    print row

cursor.execute('SELECT * FROM Pickups;')
results = cursor.fetchall()
for row in results:
    print row

cursor.execute('SELECT * FROM Bridge;')
results = cursor.fetchall()
for row in results:
    print row

cursor.execute('SELECT * FROM Body;')
results = cursor.fetchall()
for row in results:
    print row

cursor.execute('SELECT * FROM Guitar;')
results = cursor.fetchall()
for row in results:
    print row


cursor.close() """
