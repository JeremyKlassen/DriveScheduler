import sqlite3
from pathlib import Path
from Model.DB import Constants as C

class DB():
    def __init__(self):
        self.C = C.Constants()

# Getters and Setters
    def getAPIKeys(self):
        conn = sqlite3.connect(self.C.DBPATH)
        c = conn.cursor()
        c.execute('SELECT * FROM keys;')
        newKeys = c.fetchall()
        return newKeys

    def getUser(self,table,id):
        sql = "SELECT * FROM " + table + " WHERE id = " + id
        conn = sqlite3.connect(self.C.DBPATH)
        c = conn.cursor()
        c.execute(sql)
        ret = c.fetchall()
        conn.close()
        return ret

# Functionality Methods
    def addUsers(self, clients, drivers):
        conn = sqlite3.connect(self.C.DBPATH)
        c = conn.cursor()

        if clients:
            c.execute('INSERT INTO clients VALUES (?,?,?,?,?,?)', clients)
        if drivers:
            c.execute('INSERT INTO drivers VALUES (?,?,?,?,?,?)', drivers)

        conn.commit()
        conn.close()

    def createDB(self):
        myFile = Path(self.C.DBPATH)
        if myFile.is_file():
            print("Client DB Already exists.")
            return
        
        conn = sqlite3.connect(self.C.DBPATH)
        c = conn.cursor()
        c.execute(''' CREATE TABLE clients
            (id INTEGER PRIMARY KEY AUTOINCREMENT, lName TEXT, fName TEXT, pc TEXT, lat TEXT, long TEXT)''')

        c.execute(''' CREATE TABLE drivers
            (id INTEGER PRIMARY KEY AUTOINCREMENT, lName TEXT, fName TEXT, pc TEXT, lat TEXT, long TEXT)''')

        c.execute(''' CREATE TABLE keys
            (keyType text, key text)''')

        conn.commit()
        conn.close()

    def updateUser(self,update, table, id):
        sql = "UPDATE " + table + " SET lat = " + update[0] + ", long = " + update[1] + "WHERE id = " + id
        conn = sqlite3.connect(self.C.DBPATH)
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        conn.close()

    def changeKey(self,keys):
        print("Test")
        print(self.C.DBPATH)
        conn = sqlite3.connect(self.C.DBPATH)
        c = conn.cursor()

        if keys[0]:
            c.execute(''' DELETE FROM keys
                WHERE keyType = 'API_ID'; ''')
            c.execute('INSERT INTO keys VALUES (?,?)', [keys[0],keys[1]])
            self.C.API_ID = keys[0]

        if keys[1]:
            c.execute(''' DELETE FROM keys
                WHERE keyType = 'API_KEY'; ''')
            c.execute('INSERT INTO keys VALUES (?,?)', [keys[2],keys[3]])
            self.C.API_ID = keys[1]

        if keys[2]:
            c.execute(''' DELETE FROM keys
                WHERE keyType = 'PC_KEY'; ''')
            c.execute('INSERT INTO keys VALUES (?,?)', [keys[4],keys[5]])
            self.C.PC_Key = keys[2]

        conn.commit()
        conn.close()

if __name__ == '__main__':
    db = DB()
    test = db.getAPIKeys
    print(test)
    db.createDB()
    client = ['Teddy','Roosevelt','R2K']
    driver = ['Joe','Biden','R3L']
    db.addUsers(clients = client, drivers = driver)