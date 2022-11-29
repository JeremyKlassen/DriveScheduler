import sqlite3
import Constants as C
from pathlib import Path

class DB ():
    def __init__(self):
        pass

    def addUsers(self, clients, drivers):
        conn = sqlite3.connect(C.DBPATH)
        c = conn.cursor()

        if clients:
            c.execute('INSERT INTO clients VALUES (?,?,?,?)', clients)
        if drivers:
            c.execute('INSERT INTO drivers VALUES (?,?,?,?)', drivers)

        conn.commit()
        conn.close()

    

    def createDB(self):
        myFile = Path(C.DBPATH)
        if myFile.is_file():
            print("Client DB Already exists.")
            return
        
        conn = sqlite3.connect(C.DBPATH)
        c = conn.cursor()
        c.execute(''' CREATE TABLE clients
            (lName text, fName text, pc text, lat text, long text)''')

        c.execute(''' CREATE TABLE drivers
            (lName text, fName text, pc text, lat text, long text)''')

        conn.commit()
        conn.close()

if __name__ == '__main__':
    db = DB()
    db.createDB()
    client = ['Teddy','Roosevelt','52','-57']
    driver = ['Joe','Biden','52','-57']
    db.addUsers(clients = client, drivers = driver)