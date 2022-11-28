def addUsersView(clients, drivers):
    loop = True
    while loop == True:
        choice = input("1: add client, 2: add driver, 3: finished ")
        if choice == '1':
            fName = input("enter client first name: ")
            lName = input("enter client last name: ")
            lat = input("enter client lattitude: ")
            long = input("enter client longitude: ")
            t = (lName, fName, lat, long)
            clients.append(t)
        elif choice == '2':
            fName = input("enter driver first name: ")
            lName = input("enter driver last name: ")
            lat = input("enter driver lattitude: ")
            long = input("enter driver longitude: ")
            t = (lName, fName, lat, long)
            drivers.append(t)
        elif choice == '3':
            loop = False
            print("Session completed")

if __name__ == '__main__':
    clients = []
    drivers = []
    addUsersView(clients, drivers)
    print(clients)
    print(drivers)