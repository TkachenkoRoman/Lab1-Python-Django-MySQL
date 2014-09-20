import os
import sys
import MySQLdb
from load_tables_from_csv import *

guitar_types_file_path = "guitar_types.csv"
produser_file_path = "produser.csv"
pickups_file_path = "pickups.csv"
bridge_file_path = "bridge.csv"
body_file_path = "body.csv"
guitar_file_path = "guitar.csv"

guitar_db = MySQLdb.connect(host="localhost", user="root", passwd="kt315gt409", db="guitar_schema")
#  let execute the queries
db_cursor = guitar_db.cursor()
cursor = db_cursor
#loading data
load_guitar_types_from_csv(guitar_db, guitar_types_file_path, cursor, "reload")
load_produser_from_csv(guitar_db, produser_file_path, cursor, "reload")
load_pickups_from_csv(guitar_db, pickups_file_path, cursor, "reload")
load_bridge_from_csv(guitar_db, bridge_file_path, cursor, "reload")
load_body_from_csv(guitar_db, body_file_path, cursor, "reload")
load_guitar_from_csv(guitar_db, guitar_file_path, cursor, "reload")

cursor.execute('SELECT * FROM guitar_types;')
rows = cursor.fetchall()
print rows

