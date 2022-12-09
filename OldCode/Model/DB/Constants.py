import json
import sqlite3

class Constants():
    def __init__(self):
        self.conn = sqlite3.connect('Model/DB/main.db')
        self.cur = self.conn.cursor()
        # self.API_ID = self.getKeyValue('key', 'keys', 'keyType', 'API_ID')
        # self.API_KEY = self.getKeyValue('key', 'keys', 'keyType', 'API_KEY')
        # self.PS_KEY = self.getKeyValue('key', 'keys', 'keyType', 'PS_KEY')

    def getKeyValue(self, column, table, column2, value):   
        sql = "SELECT " + column + " FROM " + table + " WHERE " + column2 + " = '" + value + "';"
        try:
            self.cur.execute(sql)
        except:
            pass
        data = self.cur.fetchone()
        if not data:
            try:
                f = open('Model/DB/keys.json')
                jData = json.load(f)
                data = jData[value]
            except:
                print("No keys found in main.db or keys.json")
                return
        
        return data

    # API constants
    BASE_URL = "https://api.traveltimeapp.com/v4/routes/V4/routes"
    # PS_URL = f"""http://api.positionstack.com/v1/forward\
# ?access_key={PS_KEY}"""

    # Database constants
    DBPATH = 'Model/DB/main.db'

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
    &locations=51.45974_-0.16531,51.41494_-0.12492"""