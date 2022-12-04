import json

class Constants():
    def __init__(self):
        f = open('Model/DB/keys.json')
        data = json.load(f)
        self.API_ID = data['API_ID']
        self.API_KEY = data['API_KEY']
        self.PS_KEY = data['PS_KEY']

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

    # &app_id={API_ID}\
    # &api_key={API_KEY}"""