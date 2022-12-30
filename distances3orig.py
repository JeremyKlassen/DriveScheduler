import pandas as pd
from haversine import haversine, Unit


# Declaring Variables
clients = pd.read_excel('data.xlsx', sheet_name='clients')
drivers = pd.read_excel('data.xlsx', sheet_name='drivers')

ids = []
for i in range(len(clients.index)):
    ids.append(clients.iloc[i]["id"])
for i in range(len(drivers.index)):
    ids.append(drivers.iloc[i]["id"])

distances = pd.DataFrame(0, index=ids, columns=ids)

for i in ids:
    for j in ids:
        try:
            coords1Lat = float(clients.loc[clients["id"]==i]["lat"])
            coords1Long = float(clients.loc[clients["id"]==i]["long"])

        except:
            coords1Lat = float(drivers.loc[drivers["id"]==i]["lat"])
            coords1Long = float(drivers.loc[drivers["id"]==i]["long"])
        try:
            coords2Lat = float(clients.loc[clients["id"]==j]["lat"])
            coords2Long = float(clients.loc[clients["id"]==j]["long"])
        except:
            coords2Lat = float(drivers.loc[drivers["id"]==j]["lat"])
            coords2Long = float(drivers.loc[drivers["id"]==j]["long"])
        
        coords1 = (coords1Lat, coords1Long)
        coords2 = (coords2Lat, coords2Long)

        newDistance = int(haversine(coords1, coords2, unit=Unit.METERS))
        distances[i][j] = newDistance

with pd.ExcelWriter('data.xlsx', engine="openpyxl",if_sheet_exists="replace", mode="a") as writer:
    distances.to_excel(writer, sheet_name='distances', index=True)