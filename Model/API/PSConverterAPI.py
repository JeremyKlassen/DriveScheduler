import json
import requests
from Model.DB import Constants

# returns coordinates from a user inputed address string

class PSConverterAPI():
    def __init__(self):
        self.Constants = Constants.Constants()

    def APICall(self, address):
        try:
            #make call
            url = self.Constants.PS_URL + "&query=" + address
            response = requests.get(url)

            #parse response down to lat and long
            data = json.loads(response.text)
            data1 = data['data']
            data2 = data1[0]
            lat = data2["latitude"]
            long = data2["longitude"]
            print(lat)
            print(long)
            return (lat,long)
        except:
            print("There was an issue with the request")
            return {0,0}

if __name__ == '__main__':
    PSC = PSConverterAPI()
    PSC.APICall()