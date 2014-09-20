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