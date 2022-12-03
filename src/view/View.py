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
                pc = input("enter client postalcode (6 characters exactly with uppercase letters): ")
                t = (lName, fName, pc, 0, 0)
                clients.append(t)
            elif choice == '2':
                fName = input("enter driver first name: ")
                lName = input("enter driver last name: ")
                pc = input("enter client postalcode (6 characters exactly with uppercase letters): ")
                t = (lName, fName, pc, 0, 0)
                drivers.append(t)
            elif choice == '3':
                looper = False
                print("Session completed")

    def changeKeysView(self):
        print("If no change is required then leave entry blank")
        newAPI_ID = input("Enter Travel Time App ID: ")
        newAPI_KEY = input("Enter Travel Time Key: ")
        newPC_KEY = input("Enter Open Weather App Key: ")
        values = ["0", newAPI_ID, "1", newAPI_KEY, "2", newPC_KEY]
        return values
