from datetime import datetime, timezone
import requests
import json
import pandas as pd
import numpy   
import os
import traveltimepy as ttpy

# Declaring Variables
clients = pd.read_excel('data.xlsx', sheet_name='clients')
drivers = pd.read_excel('data.xlsx', sheet_name='drivers')
keys = pd.read_excel('data.xlsx', sheet_name='keys')
distances = pd.read_excel('data.xlsx', sheet_name='distances')
API_KEY = keys.iloc[1]['api']
API_ID = keys.iloc[2]['api']

os.environ["TRAVELTIME_ID"] = API_ID
os.environ["TRAVELTIME_KEY"] = API_KEY

locations = [
  {"id": "London center", "coords": {"lat": 51.508930, "lng": -0.131387}},
  {"id": "Hyde Park", "coords": {"lat": 51.508824, "lng": -0.167093}},
  {"id": "ZSL London Zoo", "coords": {"lat": 51.536067, "lng": -0.153596}}
]

departure_search = {
  "id": "departure search example",
  "departure_location_id": "London center",
  "arrival_location_ids": ["Hyde Park", "ZSL London Zoo"],
  "transportation": {"type": "driving"},
  "departure_time":  datetime.now(timezone.utc).isoformat(),
  "properties": ["travel_time", "distance"]
}

arrival_search = {
  "id": "arrival  search example",
  "departure_location_ids": ["Hyde Park", "ZSL London Zoo"],
  "arrival_location_id": "London center",
  "transportation": {"type": "driving"},
  "arrival_time":  datetime.now(timezone.utc).isoformat(),
  "properties": ["travel_time", "distance"],
  "range": {"enabled": True, "max_results": 1, "width": 1800}
}

out = ttpy.routes(
  locations=locations, departure_searches=departure_search, arrival_searches=arrival_search)

print(type(out))
print(out)