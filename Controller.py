from Model.DB import DB
from Model.DB import Constants as C
import Model.API.DistanceAPI as DApi
import Model.API.PSConverterAPI as PSApi

from View import View as V

class Controller:
    def __init__(self):
        self.C = C.Constants()
        self.DB = DB.DB()
        self.V = V.View()
        self.PS = PSApi.PSConverterAPI()

    def triggerChangeKeys(self):
        keys = self.V.changeKeysView()
        self.DB.changeKey(keys)

    def triggerCreateDB(self):
        self.DB.createDB()

    def triggerPSConverterAPI(self):
        coords = self.PS.APICall("528 Wellington Ave Winnipeg Manitoba")



if __name__ == '__main__':
    # cont = Controller(self)
    con = C.Constants()
    print(con.API_KEY)
    # cont.triggerPSConverterAPI()
    # cont.triggerCreateDB()
    # cont.triggerChangeKeys()