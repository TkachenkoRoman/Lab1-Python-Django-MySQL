import __init__

def generate_data(table_name, columns):
    data = []
    __init__.cursor.execute("SELECT * FROM " + table_name + ";")
    rows = __init__.cursor.fetchall()
    for row in rows:
        if row:
            curr = {}
            for i in range(row.__len__()):
                if i < columns.__len__():
                    curr[columns[i]] = row[i]
            data.append(dict(curr))
    return data

def get_guitar(id):
    __init__.cursor.execute("SELECT * FROM Guitar WHERE id=" + id + ";")
    return __init__.cursor.fetchone()

def update_guitar(id, name, strings, price, neck_material, fretboard_material):
    __init__.cursor.execute("UPDATE Guitar SET name=%s, string_amount=%s, price=%s, neck_material=%s, Fretboard_material=%s WHERE id=%s", (name, strings, price, neck_material, fretboard_material, id))
    __init__.guitar_db.commit()