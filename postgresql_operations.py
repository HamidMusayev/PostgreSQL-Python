import psycopg2


def createtable():
    conn = psycopg2.connect("dbname='datalearn' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(id INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()


def insert(roll, name, mark):
    conn = psycopg2.connect("dbname='datalearn' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)", (roll, name, mark))
    conn.commit()
    conn.close()


# insert(2, "hemidvs", 24.0)

def view():
    conn = psycopg2.connect("dbname='datalearn' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


# print(view())

def delete(id):
    conn = psycopg2.connect("dbname='datalearn' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE id=%s", (id,))
    conn.commit()
    conn.close()


# delete(1)

def update(id, name, marks):
    conn = psycopg2.connect("dbname='datalearn' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=%s, marks=%s WHERE id=%s", (name, marks, id))
    conn.commit()
    conn.close()


# update(4, "nemo", 24.0)
