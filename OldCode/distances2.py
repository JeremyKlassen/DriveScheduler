import requests
import json
import pandas as pd

# Declaring Variables
clients = pd.read_excel('data.xlsx', sheet_name='clients')
drivers = pd.read_excel('data.xlsx', sheet_name='drivers')
keys = pd.read_excel('data.xlsx', sheet_name='keys')
distances = pd.read_excel('data.xlsx', sheet_name='distances')
API_KEY = keys.iloc[1]['api']
BASE_URL = f"https://graphhopper.com/api/1/matrix?key={API_KEY}"
MAX_CALL_COUNT = 10
clientCount = len(clients.index)
driverCount = len(drivers.index)

# API Call function
def triggerAPI():
    pass

fromPoints = []
fromPointsHints = []
toPoints = []
toPointsHints = []
count = 0
for row in clients.iterrows():
    toPoints.append([row[1]["lat"],row[1]["long"]])
    toPointsHints.append(row[1]["hint"])
for row in drivers.iterrows():
    fromPoints.append([row[1]["lat"],row[1]["long"]])
    fromPointsHints.append(row[1]["hint"])

body = {"from_points": fromPoints,"to_points": toPoints, "from_point_hints":fromPointsHints, "to_point_hints":toPointsHints,"out_arrays": ["times","distances"],"vehicle": "car"}

print(body)

test = {"from_points": [[40.205816000000000000, -74.786257000000000000], [49.916362000000000000, -97.069523000000000000], [49.93366000000000000, -97.094491000000000000], [49.812044000000000000, -97.154776000000000000]], "to_points": [[49.885172000000000000, -97.16394000000000000], [41.692399000000000000, -86.267067000000000000], [49.927645000000000000, -97.104487000000000000], [49.858765000000000000, -97.265191000000000000], [49.949193000000000000, -97.189682000000000000]], "out_arrays": ["times", "distances"], "vehicle": "car"}

# print(body)

example = {"from_points": [[-0.11379003524780275,51.53664617804063],[-0.10866165161132814,51.538621486960956],[-0.11059284210205078,51.53245503603458]],"to_points": [[-0.11379003524780275,51.53664617804063],[-0.10866165161132814,51.538621486960956],[-0.11059284210205078,51.53245503603458]],"out_arrays": ["times","distances"],"vehicle": "car"}

response = requests.post(BASE_URL, json=body)
data = json.loads(response.text)
print("before")
print(data)
# print("after")
# print(type(response))
# f = open('data.json', 'wb')
# f.write(response)
# f.close()