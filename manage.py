#!/usr/bin/env python
import os
import sys
import MySQLdb
import csv

guitar_types_file_path = "guitar_types.csv"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Lab1.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

guitar_db = MySQLdb.connect(host="localhost", user="root", passwd="kt315gt409", db="guitar_schema")
#  let execute the queries
db_cursor = guitar_db.cursor()
cursor = db_cursor

def load_guitar_types_from_csv(path, cursor, mode):     #mode delete existing "reload" or "add_to_existing"
    guitar_type_id = 0 #id is in csv file, if it already exist table wont insert it
    guitar_type_id_list = []#all id`s from csv
    already_exist = () #not zero if id exist in db

    if os.path.isfile(path):
        csv_file = csv.reader(file(path), delimiter=';')

    #check if table is empty (counting rows)
    cursor.execute('SELECT COUNT(*) FROM Guitar_types;')
    is_empty = cursor.fetchone() #0 if empty
    print int(is_empty[0])

    if int(is_empty[0]): # if not 0
        if mode == "reload":
            cursor.execute('DELETE FROM guitar_types;')
            print "Elements in guitar_types were reloaded"

    for row in csv_file:
        guitar_type_id = int(row[0])
        if mode == "add_to_existing":

            #checking if id exists print a message and don`t insert new
            cursor.execute('SELECT * FROM Guitar_types WHERE id=' + str(guitar_type_id) + ";")
            already_exist = cursor.fetchone()
            if already_exist:
                print "guitar_type with id ", guitar_type_id, " already exist"
        if (guitar_type_id_list.__len__() == 0 or guitar_type_id not in guitar_type_id_list) and not already_exist:
            guitar_type_id_list.append(guitar_type_id)
            cursor.execute('INSERT INTO guitar_types(id, name)''VALUES("%i","%s");' % (guitar_type_id, row[1]))
        else:
            if mode == "reload":
                print "error guitar_type id ",guitar_type_id," already exists"
    guitar_db.commit()



#loading data
load_guitar_types_from_csv(guitar_types_file_path, cursor, "reload")

cursor.execute('SELECT * FROM guitar_types;')
results = cursor.fetchall()
for row in results:
    print row

cursor.close()