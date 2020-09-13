# 5 step way
# c = connection
# c = cursor
# execute
# c = commit
# c = close

# focusing on , and ?
# ? local/default data

# functions usage
import sqlite3


def createtable():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(id INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()


def insert(roll, name, mark):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)", (roll, name, mark))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, name, marks):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=?, marks=? WHERE id=?", (name, marks, id))
    conn.commit()
    conn.close()


update(4, 99.0, "zero")
print(view())