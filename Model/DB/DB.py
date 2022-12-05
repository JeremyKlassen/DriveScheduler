import sqlite3
from pathlib import Path
from Model.DB import Constants as C

class DB():
    def __init__(self):
        self.C = C.Constants()
        self.conn = sqlite3.connect(self.C.DBPATH)
        self.c = self.conn.cursor()

# Getters and Setters
    def getAPIKeys(self):
        self.c.execute('SELECT * FROM keys;')
        newKeys = self.c.fetchall()
        return newKeys

    def getUser(self,table,id):
        sql = "SELECT * FROM " + table + " WHERE id = " + id
        self.c.execute(sql)
        ret = self.c.fetchall()
        return ret

# Functionality Methods
    def addUsers(self, clients, drivers):
        if clients:
            self.c.execute('INSERT OR IGNORE INTO clients VALUES (?,?,?,?,?,?)', clients)
        if drivers:
            self.c.execute('INSERT OR IGNORE INTO drivers VALUES (?,?,?,?,?,?)', drivers)

        self.conn.commit()

    def createDB(self):

        self.c.execute(''' CREATE TABLE IF NOT EXISTS clients
            (id INTEGER PRIMARY KEY AUTOINCREMENT, lName TEXT, fName TEXT, pc TEXT, lat TEXT, long TEXT)''')
        self.c.execute(''' CREATE TABLE IF NOT EXISTS drivers
            (id INTEGER PRIMARY KEY AUTOINCREMENT, lName TEXT, fName TEXT, pc TEXT, lat TEXT, long TEXT)''')
        self.c.execute(''' CREATE TABLE IF NOT EXISTS keys
            (keyType text, key text)''')
        self.c.execute(''' CREATE TABLE IF NOT EXISTS distances
            (id INTEGER PRIMARY KEY AUTOINCREMENT, distance INTEGER, clientId INTEGER, driverId INTEGER)''')

        self.conn.commit()

    def updateUser(self,update, table, id):
        sql = "UPDATE " + table + " SET lat = " + update[0] + ", long = " + update[1] + "WHERE id = " + id
        self.c.execute(sql)
        self.conn.commit()

    def changeKey(self,keys):

        if keys[0]:
            self.c.execute(''' DELETE FROM keys
                WHERE keyType = 'API_ID'; ''')
            self.c.execute('INSERT INTO keys VALUES (?,?)', [keys[0],keys[1]])
            self.C.API_ID = keys[0]
        if keys[1]:
            self.c.execute(''' DELETE FROM keys
                WHERE keyType = 'API_KEY'; ''')
            self.c.execute('INSERT INTO keys VALUES (?,?)', [keys[2],keys[3]])
            self.C.API_ID = keys[1]
        if keys[2]:
            self.c.execute(''' DELETE FROM keys
                WHERE keyType = 'PC_KEY'; ''')
            self.c.execute('INSERT INTO keys VALUES (?,?)', [keys[4],keys[5]])
            self.C.PC_Key = keys[2]

        self.conn.commit()

if __name__ == '__main__':
    db = DB()
    test = db.getAPIKeys
    db.createDB()
    client = ['Teddy','Roosevelt','R2K']
    driver = ['Joe','Biden','R3L']
    db.addUsers(clients = client, drivers = driver)