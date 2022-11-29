import sqlite3
from model.Constants import Constants as C
from pathlib import Path

class DB():
    def __init__(self):
        pass

# Getters and Setters
    def getAPIKeys(self):
        conn = sqlite3.connect(C.DBPATH)
        c = conn.cursor()
        c.execute('SELECT * FROM keys;')
        newKeys = c.fetchall()
        return newKeys

# Functionality Methods
    def addUsers(self, clients, drivers):
        conn = sqlite3.connect(C.DBPATH)
        c = conn.cursor()

        if clients:
            c.execute('INSERT INTO clients VALUES (?,?,?,0,0)', clients)
        if drivers:
            c.execute('INSERT INTO drivers VALUES (?,?,?,0,0)', drivers)

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

        c.execute(''' CREATE TABLE keys
            (keyType text, key text)''')

        conn.commit()
        conn.close()

    def changeKey(self,keys):
        conn = sqlite3.connect(C.DBPATH)
        c = conn.cursor()

        if not keys[0]:
            c.execute(''' DELETE FROM keys
                WHERE keyType = 'API_ID'; ''')
            c.execute('INSERT INTO keys VALUES (?)', keys[0])
            C.API_ID = keys[0]

        if not keys[1]:
            c.execute(''' DELETE FROM keys
                WHERE keyType = 'API_KEY'; ''')
            c.execute('INSERT INTO keys VALUES (?)', keys[1])
            C.API_ID = keys[1]

        if not keys[2]:
            c.execute(''' DELETE FROM keys
                WHERE keyType = 'PC_KEY'; ''')
            c.execute('INSERT INTO keys VALUES (?)', keys[2])
            C.PC_Key = keys[2]

if __name__ == '__main__':
    db = DB()
    test = db.getAPIKeys
    print(test)
    # db.createDB()
    # client = ['Teddy','Roosevelt','R2K']
    # driver = ['Joe','Biden','R3L']
    # db.addUsers(clients = client, drivers = driver)