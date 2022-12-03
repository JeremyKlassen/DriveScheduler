from model.DB import DB
from model.DB import Constants as C
import model.DistanceAPI as DApi
import model.PCConverterAPI as PCApi

from view.View import View as V

class Controller:
    def __init__(self):
        self.C = C()
        self.DB = DB()
        self.V = V()

    def triggerChangeKeys(self):
        keys = self.V.changeKeysView()
        print(keys)
        self.DB.changeKey(keys)

    def triggerCreateDB(self):
        self.DB.createDB()

    def main (self):
        print("Hello World")

if __name__ == '__main__':
    cont = Controller()
    cont.triggerCreateDB()
    cont.triggerChangeKeys()