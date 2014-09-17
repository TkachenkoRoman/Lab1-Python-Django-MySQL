import os
import MySQLdb
import csv

def load_guitar_types_from_csv(guitar_db, path, cursor, mode):     #mode delete existing "reload" or "add_to_existing"
    id = 0 #id is in csv file, if it already exist table wont insert it
    id_list = []#all id`s from csv
    already_exist = () #not zero if id exist in db

    if os.path.isfile(path):
        csv_file = csv.reader(file(path), delimiter=';')
    else:
        print "no file ", path, " exist"
        return

    #check if table is empty (counting rows)
    cursor.execute('SELECT COUNT(*) FROM Guitar_types;')
    is_empty = cursor.fetchone() #0 if empty
    print int(is_empty[0])

    if int(is_empty[0]): # if not 0
        if mode == "reload":
            cursor.execute('DELETE FROM guitar_types;')
            print "Elements in guitar_types were reloaded"

    for row in csv_file:
        if not row: #pass emty rows
            continue
        id = int(row[0])
        if mode == "add_to_existing":

            #checking if id exists print a message and don`t insert new
            cursor.execute('SELECT * FROM Guitar_types WHERE id=' + str(id) + ";")
            already_exist = cursor.fetchone()
            if already_exist:
                print "guitar_type with id ", id, " already exist"
        if (id_list.__len__() == 0 or id not in id_list) and not already_exist:
            id_list.append(id)
            cursor.execute('INSERT INTO guitar_types(id, name)''VALUES("%i","%s");' % (id, row[1]))
        else:
            if mode == "reload":
                print "error guitar_type id ",id," already exists"
    guitar_db.commit()

def load_produser_from_csv(guitar_db, path, cursor, mode):
    id = 0 #id is in csv file, if it already exist table wont insert it
    id_list = []#all id`s from csv
    already_exist = () #not zero if id exist in db

    if os.path.isfile(path):
        csv_file = csv.reader(file(path), delimiter=';')
    else:
        print "no file ", path, " exist"
        return
    #check if table is empty (counting rows)
    cursor.execute('SELECT COUNT(*) FROM Produser;')
    is_empty = cursor.fetchone() #0 if empty
    print int(is_empty[0])

    if int(is_empty[0]): # if not 0
        if mode == "reload":
            cursor.execute('DELETE FROM Produser;')
            print "Elements in produser were reloaded"

    for row in csv_file:
        if not row: #pass emty rows
            continue
        id = int(row[0])
        if mode == "add_to_existing":

            #checking if id exists print a message and don`t insert new
            cursor.execute('SELECT * FROM Produser WHERE id=' + str(id) + ";")
            already_exist = cursor.fetchone()
            if already_exist:
                print "produser with id ", id, " already exist"
        if (id_list.__len__() == 0 or id not in id_list) and not already_exist:
            id_list.append(id)
            cursor.execute('INSERT INTO Produser(id, name, rating, guitar, bridge, pickups, info)''VALUES("%i","%s", "%i", "%s", "%s", "%s", "%s");' % (id, row[1], int(row[2]), row[3], row[4], row[5], row[6]))
        else:
            if mode == "reload":
                print "error produser id ",id," already exists"
    guitar_db.commit()

def load_pickups_from_csv(guitar_db, path, cursor, mode):
    id = 0 #id is in csv file, if it already exist table wont insert it
    id_list = []#all id`s from csv
    already_exist = () #not zero if id exist in db

    if os.path.isfile(path):
        csv_file = csv.reader(file(path), delimiter=';')
    else:
        print "no file ", path, " exist"
        return

    #check if table is empty (counting rows)
    cursor.execute('SELECT COUNT(*) FROM Pickups;')
    is_empty = cursor.fetchone() #0 if empty
    print int(is_empty[0])

    if int(is_empty[0]): # if not 0
        if mode == "reload":
            cursor.execute('DELETE FROM Pickups;')
            print "Elements in pickups were reloaded"

    for row in csv_file:
        if not row: #pass emty rows
            continue
        id = int(row[0])
        if mode == "add_to_existing":

            #checking if id exists print a message and don`t insert new
            cursor.execute('SELECT * FROM Pickups WHERE id=' + str(id) + ";")
            already_exist = cursor.fetchone()
            if already_exist:
                print "pickups with id ", id, " already exist"
        if (id_list.__len__() == 0 or id not in id_list) and not already_exist:
            cursor.execute('SELECT * FROM Produser WHERE id=' + row[1] + ";")
            produser = cursor.fetchone()#none if no produser found
            if produser:
                id_list.append(id)
                cursor.execute('INSERT INTO Pickups(id, produser_id, type, set_type)''VALUES("%i","%i", "%s", "%s");' % (id, int(row[1]), row[2], row[3]))
            else:
                print "no produser with id ", int(row[1]), " found"
        else:
            if mode == "reload":
                print "error pickups id ",id," already exists"
    guitar_db.commit()

def load_bridge_from_csv(guitar_db, path, cursor, mode):
    id = 0 #id is in csv file, if it already exist table wont insert it
    id_list = []#all id`s from csv
    already_exist = () #not zero if id exist in db

    if os.path.isfile(path):
        csv_file = csv.reader(file(path), delimiter=';')
    else:
        print "no file ", path, " exist"
        return

    #check if table is empty (counting rows)
    cursor.execute('SELECT COUNT(*) FROM Bridge;')
    is_empty = cursor.fetchone() #0 if empty
    print int(is_empty[0])

    if int(is_empty[0]): # if not 0
        if mode == "reload":
            cursor.execute('DELETE FROM Bridge;')
            print "Elements in bridge were reloaded"

    for row in csv_file:
        if not row: #pass emty rows
            continue
        id = int(row[0])
        if mode == "add_to_existing":

            #checking if id exists print a message and don`t insert new
            cursor.execute('SELECT * FROM Bridge WHERE id=' + str(id) + ";")
            already_exist = cursor.fetchone()
            if already_exist:
                print "bridge with id ", id, " already exist"
        if (id_list.__len__() == 0 or id not in id_list) and not already_exist:
            cursor.execute('SELECT * FROM Produser WHERE id=' + row[4] + " and bridge=1" + ";")
            produser = cursor.fetchone()#none if no produser found
            if produser:
                id_list.append(id)
                cursor.execute('INSERT INTO Bridge(id, name, material, color, produser_id)''VALUES("%i","%s", "%s", "%s", "%i");' % (id, row[1], row[2], row[3], int(row[4])))
            else:
                print "no produser with id ", int(row[4]), " found or it doesn`t produse bridges"
        else:
            if mode == "reload":
                print "error bridge id ",id," already exists"
    guitar_db.commit()

def load_body_from_csv(guitar_db, path, cursor, mode):
    id = 0 #id is in csv file, if it already exist table wont insert it
    id_list = []#all id`s from csv
    already_exist = () #not zero if id exist in db

    if os.path.isfile(path):
        csv_file = csv.reader(file(path), delimiter=';')
    else:
        print "no file ", path, " exist"
        return

    #check if table is empty (counting rows)
    cursor.execute('SELECT COUNT(*) FROM Body;')
    is_empty = cursor.fetchone() #0 if empty
    print int(is_empty[0])

    if int(is_empty[0]): # if not 0
        if mode == "reload":
            cursor.execute('DELETE FROM Body;')
            print "Elements in Body were reloaded"

    for row in csv_file:
        if not row: #pass emty rows
            continue
        id = int(row[0])
        if mode == "add_to_existing":

            #checking if id exists print a message and don`t insert new
            cursor.execute('SELECT * FROM Body WHERE id=' + str(id) + ";")
            already_exist = cursor.fetchone()
            if already_exist:
                print "Body with id ", id, " already exist"
        if (id_list.__len__() == 0 or id not in id_list) and not already_exist:
            id_list.append(id)
            cursor.execute('INSERT INTO Body(id, material, color, type, form)''VALUES("%i","%s", "%s", "%s", "%s");' % (id, row[1], row[2], row[3], row[4]))
        else:
            if mode == "reload":
                print "error Body id ",id," already exists"
    guitar_db.commit()

def load_guitar_from_csv(guitar_db, path, cursor, mode):
    id = 0 #id is in csv file, if it already exist table wont insert it
    id_list = []#all id`s from csv
    already_exist = () #not zero if id exist in db

    if os.path.isfile(path):
        csv_file = csv.reader(file(path), delimiter=';')
    else:
        print "no file ", path, " exist"
        return

    #check if table is empty (counting rows)
    cursor.execute('SELECT COUNT(*) FROM Guitar;')
    is_empty = cursor.fetchone() #0 if empty
    print int(is_empty[0])

    if int(is_empty[0]): # if not 0
        if mode == "reload":
            cursor.execute('DELETE FROM Guitar;')
            print "Elements in Guitar were reloaded"

    for row in csv_file:
        if not row: #pass emty rows
            continue
        cursor.execute('SELECT * FROM Guitar_types WHERE id=' + row[6] + ";")
        type = cursor.fetchone()#none if no type found
        cursor.execute('SELECT * FROM Body WHERE id=' + row[7] + ";")
        body = cursor.fetchone()
        cursor.execute('SELECT * FROM Bridge WHERE id=' + row[8] + ";")
        bridge = cursor.fetchone()
        cursor.execute('SELECT * FROM Pickups WHERE id=' + row[9] + ";")
        pickups = cursor.fetchone()
        cursor.execute('SELECT * FROM Produser WHERE id=' + row[10] + ";")
        produser = cursor.fetchone()
        if type and body and bridge and pickups and produser:
            cursor.execute('INSERT INTO Guitar(name, string_amount, price, neck_material,\
                            Fretboard_material, Pick_guard, Type_id, Body_id, Bridge_id,\
                             Pickups_id, Guitar_produser_id)'\
                           'VALUES("%s","%i", "%i", "%s", "%s", "%s", "%i", "%i", "%i","%i","%i");'\
                           % (row[0], int(row[1]), int(row[2]), row[3], row[4], row[5], int(row[6]),\
                           int(row[7]), int(row[8]), int(row[9]), int(row[10])))
        else:
            print "no produser or pickups or type or bridge id found"

    guitar_db.commit()