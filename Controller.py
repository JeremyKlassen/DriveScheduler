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
        print(coords)



if __name__ == '__main__':
    cont = Controller()
    # cont.DB.createDB()
    def copyKeysToDB():
        tAPI_KEY = cont.DB.Constants.getKeyValue('key', 'keys', 'KeyType', 'API_KEY')
        tAPI_ID = cont.DB.Constants.getKeyValue('key', 'keys', 'KeyType', 'API_ID')
        tPS_KEY = cont.DB.Constants.getKeyValue('key', 'keys', 'KeyType', 'PS_KEY')
        keys = (tAPI_KEY, tAPI_ID, tPS_KEY)
        keyIDs = ('API_KEY', 'API_ID', 'PS_KEY')
        cont.DB.addKeys(keys,keyIDs)
    
    copyKeysToDB()
        
    
