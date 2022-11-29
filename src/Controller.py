# from model.Constants import Constants as C
from model.DB import DB
from view.View import View

class Controller:
    def __init__(self):
        pass

    def triggerChangeAPI(self):
        keys = View.changeKeysView(self)
        DB.changeKey(self,keys=keys)

    def main (self):
        print("Hello World")

if __name__ == '__main__':
    cont = Controller()
    # cont.triggerChangeAPI()
    print(DB.getAPIKeys)