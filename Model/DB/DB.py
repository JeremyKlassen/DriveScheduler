import sqlite3
from pathlib import Path
from Model.DB import Constants

class DB():
    def __init__(self):
        self.Constants = Constants.Constants()
        self.conn = sqlite3.connect(self.Constants.DBPATH)
        self.cur = self.conn.cursor()

# Getting data
    def getAPIKeys(self):
        self.cur.execute('SELECT * FROM keys;')
        newKeys = self.cur.fetchall()
        return newKeys

    def getUser(self,table,id):
        sql = "SELECT * FROM " + table + " WHERE id = " + id
        self.cur.execute(sql)
        ret = self.cur.fetchall()
        return ret

# Functionality Methods

# DB Creation
    def createDB(self):

        self.cur.execute(''' CREATE TABLE IF NOT EXISTS clients
            (id INTEGER PRIMARY KEY AUTOINCREMENT, lName TEXT, fName TEXT, pc TEXT, lat TEXT, long TEXT)''')
        self.cur.execute(''' CREATE TABLE IF NOT EXISTS drivers
            (id INTEGER PRIMARY KEY AUTOINCREMENT, lName TEXT, fName TEXT, pc TEXT, lat TEXT, long TEXT)''')
        self.cur.execute(''' CREATE TABLE IF NOT EXISTS keys
            (keyType text, key text)''')
        self.cur.execute(''' CREATE TABLE IF NOT EXISTS distances
            (id INTEGER PRIMARY KEY AUTOINCREMENT, distance INTEGER, clientId INTEGER, driverId INTEGER)''')

        self.conn.commit()

#Setting data

    def addUsers(self, clients, drivers):
        if clients:
            self.cur.execute('INSERT OR IGNORE INTO clients VALUES (?,?,?,?,?,?)', clients)
        if drivers:
            self.cur.execute('INSERT OR IGNORE INTO drivers VALUES (?,?,?,?,?,?)', drivers)

        self.conn.commit()


    def addKeys(self, keys, keyIds):
        for i in range(0, len(keys)):
            sql = "INSERT OR IGNORE INTO keys VALUES ('" + keyIds[i] + "', '" + keys[i] + "';"
            self.c.execute(sql)
        self.conn.commit()


    def updateUser(self,update, table, id):
        sql = "UPDATE " + table + " SET lat = " + update[0] + ", long = " + update[1] + "WHERE id = " + id
        self.cur.execute(sql)
        self.conn.commit()


    def changeKey(self,keys):

        if keys[0]:
            self.cur.execute(''' DELETE FROM keys
                WHERE keyType = 'API_ID'; ''')
            self.cur.execute('INSERT INTO keys VALUES (?,?)', [keys[0],keys[1]])
            self.Constants.API_ID = keys[0]
        if keys[1]:
            self.cur.execute(''' DELETE FROM keys
                WHERE keyType = 'API_KEY'; ''')
            self.cur.execute('INSERT INTO keys VALUES (?,?)', [keys[2],keys[3]])
            self.Constants.API_ID = keys[1]
        if keys[2]:
            self.cur.execute(''' DELETE FROM keys
                WHERE keyType = 'PC_KEY'; ''')
            self.cur.execute('INSERT INTO keys VALUES (?,?)', [keys[4],keys[5]])
            self.Constants.PC_Key = keys[2]

        self.conn.commit()


if __name__ == '__main__':
    db = DB()
    test = db.getAPIKeys
    db.createDB()
    client = ['Teddy','Roosevelt','R2K']
    driver = ['Joe','Biden','R3L']
    db.addUsers(clients = client, drivers = driver)