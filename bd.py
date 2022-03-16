import sqlite3
from sqlite3 import Error


def initbd():
    """Init bd"""
    
    try:
        conn = sqlite3.connect("file")
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    
