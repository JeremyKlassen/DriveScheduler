import pandas as pd
import json
import requests
import numpy    

#read spreadsheets to dataframes
clients = pd.read_excel('data.xlsx', sheet_name='clients')
drivers = pd.read_excel('data.xlsx', sheet_name='drivers')
keys = pd.read_excel('data.xlsx', sheet_name='keys')

#variable creation
key = keys.loc[0][1]
PS_URL = f"""http://api.positionstack.com/v1/forward\
?access_key={key}"""
address = ""
clientsLength = len(clients.index)
driversLength = len(drivers.index)

#iterate over clients dataframe to put coordinates into dataframe
def iterClients():
    for i in range(0,clientsLength):
        if numpy.any(clients.iloc[i]['lat']) and numpy.any(clients.iloc[i]['long']):
            address = clients.loc[i]['address']
            url = PS_URL + "&query=" + address + " Winnipeg Manitoba Canada"
            response = requests.get(url)
            data = json.loads(response.text)
            data1 = data['data']
            data2 = data1[0]
            lat = data2["latitude"]
            long = data2["longitude"]
            confidence = data2["confidence"]

            if confidence < 0.8:
                fName = clients.iloc[i]['fName']
                lName = clients.iloc[i]['lName']
                print("low confidence in this result for " + fName + " " + lName + ". Please enter the coordinates: ")
                print(lat + " " + long)
                print("into google maps to verify correct location.")

            clients.at[i, 'lat'] = lat
            clients.at[i, 'long'] = long
        else:
            print("There already exists coordinates for " + clients.iloc[i]['fName'] + " " + clients.iloc[i]['lName'])

#iterate over drivers dataframe to put coordinates into dataframe
def iterDrivers():
    for i in range(0,driversLength):
        if numpy.any(drivers.iloc[i]['lat']) and numpy.any(drivers.iloc[i]['long']) :
            address = drivers.loc[i]['address']
            url = PS_URL + "&query=" + address + " Winnipeg Manitoba Canada"
            response = requests.get(url)
            data = json.loads(response.text)
            data1 = data['data']
            data2 = data1[0]
            lat = data2["latitude"]
            long = data2["longitude"]
            confidence = data2["confidence"]

            if confidence < 0.8:
                fName = drivers.iloc[i]['fName']
                lName = drivers.iloc[i]['lName']
                print("low confidence in this result for " + fName + " " + lName + ". Please enter the coordinates: ")
                print(lat + " " + long)
                print("into google maps to verify correct location.")

            drivers.at[i, 'lat'] = lat
            drivers.at[i, 'long'] = long
        else:
            print("There already exists coordinates for " + drivers.iloc[i]['fName'] + " " + drivers.iloc[i]['lName'])

#write coordinates found into client and drivers spreadsheets.
def WritePD():
    with pd.ExcelWriter('data.xlsx', engine="openpyxl",if_sheet_exists="replace", mode="a") as writer:
        clients.to_excel(writer, sheet_name='clients', index=False)
        drivers.to_excel(writer, sheet_name='drivers', index=False)

iterClients()
iterDrivers()
WritePD()