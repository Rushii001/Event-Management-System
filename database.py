import sqlite3

def connect():
    conn = sqlite3.connect("events.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    date TEXT,
                    location TEXT)""")
    conn.commit()
    conn.close()

def insert(name, date, location):
    conn = sqlite3.connect("events.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO events VALUES (NULL,?,?,?)", (name, date, location))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("events.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM events")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("events.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM events WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, date, location):
    conn = sqlite3.connect("events.db")
    cur = conn.cursor()
    cur.execute("UPDATE events SET name=?, date=?, location=? WHERE id=?", (name, date, location, id))
    conn.commit()
    conn.close() 


