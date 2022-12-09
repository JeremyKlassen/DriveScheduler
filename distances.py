from datetime import datetime, timezone
import requests
import json
import pandas as pd
import numpy   
import os
import traveltimepy as ttpy
import copy

# Declaring Variables
clients = pd.read_excel('data.xlsx', sheet_name='clients')
drivers = pd.read_excel('data.xlsx', sheet_name='drivers')
keys = pd.read_excel('data.xlsx', sheet_name='keys')
distances = pd.read_excel('data.xlsx', sheet_name='distances')
API_KEY = keys.iloc[1]['api']
API_ID = keys.iloc[2]['api']

os.environ["TRAVELTIME_ID"] = API_ID
os.environ["TRAVELTIME_KEY"] = API_KEY
locations = []

# Build out locations array
for row in clients.iterrows():
  id = row[1][0]
  lat = row[1][4]
  long = row[1][5]
  coords = {"lat":lat,"lng":long}
  nextLoc = {"id":id,"coords":coords}
  locations.append(nextLoc)

for row in drivers.iterrows():
  id = row[1][0]
  lat = row[1][4]
  long = row[1][5]
  coords = {"lat":lat,"lng":long}
  nextLoc = {"id":id,"coords":coords}
  locations.append(nextLoc)


for row in drivers.iterrows():
  arrivalLocations = copy.deepcopy(locations)
  arrivalLocations.remove(row[1][0])


  departure_search = {
    "id": "drives",
    "departure_location_id": row[1][0],
    "arrival_location_ids": locations,
    "transportation": {"type": "driving"},
    "departure_time":  datetime.now(timezone.utc).isoformat(),
    "properties": ["travel_time", "distance"]
  }

def apiCall():
  out = ttpy.routes(
    locations=locations, departure_searches=departure_search)

  data = out['results'][0]['locations']
  print(type(data))
  print(data)
  print(data[0])
  print(data[1])