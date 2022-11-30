import sqlite3
from pathlib import Path

class DB():
    def __init__(self):
        self.C = Constants()

# Getters and Setters
    def getAPIKeys(self):
        conn = sqlite3.connect(self.C.DBPATH)
        c = conn.cursor()
        c.execute('SELECT * FROM keys;')
        newKeys = c.fetchall()
        print(newKeys)
        return newKeys

# Functionality Methods
    def addUsers(self, clients, drivers):
        conn = sqlite3.connect(self.C.DBPATH)
        c = conn.cursor()

        if clients:
            c.execute('INSERT INTO clients VALUES (?,?,?,0,0)', clients)
        if drivers:
            c.execute('INSERT INTO drivers VALUES (?,?,?,0,0)', drivers)

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
            (lName text, fName text, pc text, lat text, long text)''')

        c.execute(''' CREATE TABLE drivers
            (lName text, fName text, pc text, lat text, long text)''')

        c.execute(''' CREATE TABLE keys
            (keyType text, key text)''')

        conn.commit()
        conn.close()

    def changeKey(self,keys):
        print(keys)
        conn = sqlite3.connect(self.C.DBPATH)
        c = conn.cursor()

        if not keys[0]:
            c.execute(''' DELETE FROM keys
                WHERE keyType = 'API_ID'; ''')
            c.execute('INSERT INTO keys VALUES (?)', keys[0])
            self.C.API_ID = keys[0]

        if not keys[1]:
            c.execute(''' DELETE FROM keys
                WHERE keyType = 'API_KEY'; ''')
            c.execute('INSERT INTO keys VALUES (?)', keys[1])
            self.C.API_ID = keys[1]

        if not keys[2]:
            c.execute(''' DELETE FROM keys
                WHERE keyType = 'PC_KEY'; ''')
            c.execute('INSERT INTO keys VALUES (?)', keys[2])
            self.C.PC_Key = keys[2]

        conn.commit()
        conn.close()


class Constants():
    def __init__(self):
        pass

    # API constants
    BASE_URL = "https://api.traveltimeapp.com/v4/routes/V4/routes"
    API_ID = "e4519f0a"
    API_KEY = "db04e55a43e11768c3ba45fba5736975"
    PC_Key = "91828dbb9820eb89193ab9aa5cd070f3"
    PC_Url = "http://api.openweathermap.org/geo/1.0/zip?"

    # Database constants
    DBPATH = 'src/model/main.db'

    # Temp/Test constants
    GET_EXAMPLE = """https://api.traveltimeapp.com/v4/routes
    ?type=public_transport
    &origin_lat=51.41070
    &origin_lng=-0.15540
    &destination_lat=51.59974
    &destination_lng=-0.19531
    &arrival_time=2022-11-18T16:00:00Z
    &app_id=YOUR_APP_ID
    &api_key=YOUR_API_KEY"""

    TIME_FILTER = f"""https://api.traveltimeapp.com/v4/time-filter\
    ?type=driving\
    &arrival_time=2022-11-18T16:00:00Z\
    &search_lat=51.41070\
    &search_lng=-0.15540\
    &locations=51.45974_-0.16531,51.41494_-0.12492\
    &app_id={API_ID}\
    &api_key={API_KEY}"""

if __name__ == '__main__':
    db = DB()
    test = db.getAPIKeys
    print(test)
    # db.createDB()
    # client = ['Teddy','Roosevelt','R2K']
    # driver = ['Joe','Biden','R3L']
    # db.addUsers(clients = client, drivers = driver)