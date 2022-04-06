import sqlite3
import os



# create connect 
conn = sqlite3.connect(os.path.join("ac.db"))
cursor = conn.cursor()

  

def get_cursor():
    return cursor

def create(user_id: int, name):
    cursor.execute("SELECT * FROM User")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO User (user_id, name) VALUES (?, ?)", (user_id, name))
        conn.commit()
    else: 
        print("this entry already exist")

def find_by_id(entry_id: int):
    cursor.execute(f'SELECT * FROM User WHERE user_id = "{entry_id}"')
    out = cursor.fetchall()[0][0]
    
    conn.commit()
    return out


