import sqlite3
import Constants as C
from pathlib import Path

def createDB () :
    myFile = Path(C.DBPATH)
    if myFile.is_file():
        print("Client DB Already exists.")
        return
        
    conn = sqlite3.connect(C.DBPATH)
    c = conn.cursor()
    c.execute(''' CREATE TABLE clients
        (lName text, fName text, lat text, long text)''')

    c.execute(''' CREATE TABLE drivers
        (lName text, fName text, lat text, long text)''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    createDB()