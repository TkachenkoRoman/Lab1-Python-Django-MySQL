import __init__

def generate_data(table_name, columns):
    data = []
    guitar_table_sql = "select g.id, g.name, g.string_amount, g.price, \
                         g.neck_material, g.Fretboard_material, g.Pick_guard, \
                         g_t.name, b.material, br.name, p.set_type, prod.name\
                         from Guitar g \
                         left join Guitar_types g_t on g.Type_id = g_t.id \
                         left join body b on g.Body_id = b.id \
                         left join bridge br on g.Bridge_id = br.id \
                         left join Pickups p on g.Pickups_id = p.id \
                         left join Produser prod on g.Guitar_produser_id = prod.id"
    if table_name == "Guitar":
        __init__.cursor.execute(guitar_table_sql)
    else:
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

def del_guitar(id):
    __init__.cursor.execute("DELETE FROM Guitar WHERE id=" + id + ";")

def get_guitar(id):
    __init__.cursor.execute("SELECT * FROM Guitar WHERE id=" + id + ";")
    return __init__.cursor.fetchone()

def get_guitar_type(id):
    __init__.cursor.execute("SELECT t.id, t.name FROM Guitar g left join Guitar_types t on g.Type_id = t.id WHERE g.id=" + id + ";")
    return __init__.cursor.fetchone()

def get_guitar_types():
    __init__.cursor.execute("SELECT * FROM Guitar_types")
    return __init__.cursor.fetchall()

def update_guitar(id, name, strings, price, neck_material, fretboard_material):
    __init__.cursor.execute("UPDATE Guitar SET name=%s, string_amount=%s, price=%s, neck_material=%s, Fretboard_material=%s WHERE id=%s", (name, strings, price, neck_material, fretboard_material, id))
    __init__.guitar_db.commit()