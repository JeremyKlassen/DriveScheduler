import json
import requests
from Model.DB import Constants as C

class PSConverterAPI():
    def __init__(self):
        self.C = C.Constants()

    def APICall(self):
        # url = self.C.PS_Url + "zip=R2K2K3,CA&app_id=" + self.C.PS_Key
        url = self.C.PS_URL + "&query=1528 Ross Ave Winnipeg Manitoba"
        # print(url)
        # print("https://api.positionstack.com/v1/forward?access_key=c07c7bfcb81f2bd43816f86683976410&query=1600%20Pennsylvania%20Ave%20NW,%20Washington%20DC")
        # body = {"batch":[{"query":"1528 Ross Ave Winnipeg Manitoba","country":"CA","region":"Manitoba"}]}
        response = requests.get(url)
        print(response.text)
        # print(url)

if __name__ == '__main__':
    PSC = PSConverterAPI()
    PSC.APICall()