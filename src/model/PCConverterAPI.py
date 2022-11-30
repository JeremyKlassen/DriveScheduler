import json
import requests
from model.DB import Constants as C

class PCConverterAPI():
    def __init__(self):
        pass

    def APICall(self):
        url = C.PC_Url + "zip=R2K2K3,CA&app_id=" + C.PC_Key
        response = requests.get(url)
        print(response.text)
        # print(url)

if __name__ == '__main__':
    PCC = PCConverterAPI()
    PCC.APICall()