import  requests
import Constants as C



GET_EXAMPLE = f"""https://api.traveltimeapp.com/v4/routes?type=public_transport&origin_lat=51.41070&origin_lng=-0.15540&destination_lat=51.59974&destination_lng=-0.19531&arrival_time=2022-11-18T16:00:00Z&app_id={C.API_ID}&api_key={C.API_KEY}"""

TIME_FILTER = f"""https://api.traveltimeapp.com/v4/time-filter?type=driving&arrival_time=2022-11-18T16:00:00Z&search_lat=51.41070&search_lng=-0.15540&locations=51.45974_-0.16531,51.41494_-0.12492&app_id={C.API_ID}&api_key={C.API_KEY}"""

response = requests.get(TIME_FILTER)
new = response.content
print (response.text)