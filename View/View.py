class View():
    def __init__(self):
        pass

    def mainView(self):
        menuOption = input("1: make list , 2: to add/remove people from database, 3: to initialize Database, 4: to update distances/times, 5: to Change API Keys ")
        return menuOption

    def addUsersView(clients, drivers):
        looper = True
        while looper == True:
            choice = input("1: add client, 2: add driver, 3: finished ")
            if choice == '1':
                fName = input("enter client first name: ")
                lName = input("enter client last name: ")
                add = input("enter client Address (address city province): ")
                t = (lName, fName, add, 0, 0)
                clients.append(t)
            elif choice == '2':
                fName = input("enter driver first name: ")
                lName = input("enter driver last name: ")
                add = input("enter client Address: ")
                t = (lName, fName, add, 0, 0)
                drivers.append(t)
            elif choice == '3':
                looper = False
                print("Session completed")

    def changeKeysView(self):
        print("If no change is required then leave entry blank")
        newAPI_ID = input("Enter Travel Time App ID: ")
        newAPI_KEY = input("Enter Travel Time Key: ")
        newPS_KEY = input("Enter Position Stack Key: ")
        values = ["API_ID", newAPI_ID, "API_KEY", newAPI_KEY, "PC_KEY", newPS_KEY]
        return values
