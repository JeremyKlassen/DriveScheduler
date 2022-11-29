class View():
    def __init__(self):
        pass

    def mainView(self):
        menuOption = input("1: make list , 2: to add/remove people from database, 3: to initialize Database, 4: to update distances/times")
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

