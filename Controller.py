from Model.DB import DB
from Model.DB import Constants
import Model.API.DistanceAPI as DApi
import Model.API.PSConverterAPI as PSApi
from View import View

class Controller:
    def __init__(self):
        self.Constants = Constants.Constants()
        self.DB = DB.DB()
        self.View = View.View()
        self.PS = PSApi.PSConverterAPI()

    def triggerChangeKeys(self):
        keys = self.View.changeKeysView()
        self.DB.changeKey(keys)

    def triggerCreateDB(self):
        self.DB.createDB()

    def triggerPSConverterAPI(self):
        coords = self.PS.APICall("528 Wellington Ave Winnipeg Manitoba")



if __name__ == '__main__':
    cont = Controller()
    cont.DB.createDB()

    # print(con.API_KEY)
