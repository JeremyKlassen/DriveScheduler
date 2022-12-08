import requests
import json
from Model.DB import Constants

# Distance API Brings 

class DistanceAPI():
    def __init__(self):
        self.Constants = Constants.Constants()

    def apiCall (self):
        response = requests.get(self.Constants.TIME_FILTER)
        print (response.text)
        return response.text

    def apiToJSON (this):
        jsonData = this.apiCall()
        print (jsonData)
        times = json.loads(jsonData)
        with open("src/model/times.json", "w") as outfile:
            json.dump(this.apiCall(), outfile)

if __name__ == '__main__':
    Distance = DistanceAPI()
    Distance.apiToJSON()