import __init__

def generate_guitar_sql_query(filter_dict, order_by):
    sql = """select g.id, g.name, g.string_amount, g.price,
                         g.neck_material, g.Fretboard_material, g.Pick_guard,
                         g_t.name, b.material, br.name, p.set_type, prod.name
                         from Guitar g
                         left join Guitar_types g_t on g.Type_id = g_t.id
                         left join body b on g.Body_id = b.id
                         left join bridge br on g.Bridge_id = br.id
                         left join Pickups p on g.Pickups_id = p.id
                         left join Produser prod on g.Guitar_produser_id = prod.id"""
    prices = []
    price_range = None
    guitar_type = None
    produser = None
    if filter_dict:
        if filter_dict['price'] != '-':
            prices = filter_dict['price'].split('-')
            price_range = ' g.price >= ' + prices[0] + ' and g.price <= ' + prices[1]
        if filter_dict['type'] != '-':
            guitar_type = ' g_t.name="' + filter_dict['type'] + '"'
        if filter_dict['produser'] != '-':
            produser = ' prod.name="' + filter_dict['produser'] + '"'
    if price_range or guitar_type or produser:
        sql += ' where'
    if price_range:
        sql += price_range
        if guitar_type:
            sql += ' and '
    if guitar_type:
        sql += guitar_type
        if produser:
            sql += ' and '
    if produser:
        sql += produser
    if order_by:
        sql += " "
        sql += order_by
    return  sql

def generate_data(table_name, columns, filter_dict=None):
    data = []
    guitar_table_sql = generate_guitar_sql_query(filter_dict, "order by g.id asc")
    if table_name == "Guitar":
        __init__.cursor.execute(guitar_table_sql)
    else:
        __init__.cursor.execute("SELECT * FROM " + table_name + " order by id asc;")
    rows = __init__.cursor.fetchall()
    for row in rows:
        if row:
            curr = {}
            for i in range(row.__len__()):
                if i < columns.__len__():
                    curr[columns[i]] = row[i]
            data.append(dict(curr))
    return data

def reload_db_from_csv():
    __init__.load_from_csv()

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

def get_body(id):
    __init__.cursor.execute("SELECT b.id, b.material, b.color, b.type, b.form FROM Guitar g left join Body b on g.Body_id = b.id WHERE g.id=" + id + ";")
    return __init__.cursor.fetchone()

def get_bodies():
    __init__.cursor.execute("SELECT * FROM Body")
    return __init__.cursor.fetchall()

def get_bridge(id):
    __init__.cursor.execute("SELECT b.id, b.name, b.material, b.color, p.name FROM Guitar g \
                              left join Bridge b on g.Bridge_id = b.id left join Produser p on b.produser_id = p.id\
                               WHERE g.id=" + id + ";")
    return __init__.cursor.fetchone()

def get_bridges():
    __init__.cursor.execute("SELECT b.id, b.name, b.material, b.color, p.name FROM Bridge b left join Produser p on b.produser_id = p.id")
    return __init__.cursor.fetchall()

def get_pickup(id):
    __init__.cursor.execute("SELECT p.id, p.type, p.set_type, pr.name FROM Guitar g \
                              left join Pickups p on g.Pickups_id = p.id left join Produser pr on p.produser_id = pr.id\
                               WHERE g.id=%s", id)
    return __init__.cursor.fetchone()

def get_pickups():
    __init__.cursor.execute("SELECT p.id, p.type, p.set_type, pr.name FROM Pickups p \
                              left join Produser pr on p.produser_id = pr.id")
    return __init__.cursor.fetchall()

def get_produser(id):
    __init__.cursor.execute("SELECT p.id, p.name, p.rating FROM Guitar g left join Produser p on g.Guitar_produser_id = p.id WHERE g.id=" + id + ";")
    return __init__.cursor.fetchone()

def get_produsers():
    __init__.cursor.execute("SELECT p.id, p.name, p.rating FROM Produser p WHERE p.guitar=true")
    return __init__.cursor.fetchall()

def get_pickguard(id):
    __init__.cursor.execute("SELECT Pick_guard FROM Guitar WHERE id=" + id + ";")
    return __init__.cursor.fetchone()

def update_guitar(id, name, strings, price, neck_material, fretboard_material, type, body, bridge, pickups, produser, pickguard):
    if not strings:
        strings = 0
    if not price:
        price = 0
    if pickguard == 'on':
        pickguard = 1
    else:
        pickguard = 0
    __init__.cursor.execute("UPDATE Guitar SET name=%s, string_amount=%s, price=%s, neck_material=%s, \
                              Fretboard_material=%s, Type_id=%s, Body_id=%s, Bridge_id=%s, Pickups_id=%s, Guitar_produser_id=%s, Pick_guard=%s WHERE id=%s", \
                            (name, strings, price, neck_material, fretboard_material, type, body, bridge, pickups, produser, pickguard, id))
    __init__.guitar_db.commit()

def insert_guitar(name, strings, price, neck_material, fretboard_material, type, body, bridge, pickups, produser, pickguard):
    if not strings:
        strings = 0
    if not price:
        price = 0
    if pickguard == 'on':
        pickguard = 1
    else:
        pickguard = 0
    __init__.cursor.execute('INSERT INTO Guitar(name, string_amount, price, neck_material,\
                            Fretboard_material, Type_id, Body_id, Bridge_id,\
                             Pickups_id, Guitar_produser_id, Pick_guard)'\
                           'VALUES("%s","%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s","%s");'\
                           % (name, strings, price, neck_material, fretboard_material, type, body,\
                           bridge, pickups, produser, pickguard))
    __init__.guitar_db.commit()