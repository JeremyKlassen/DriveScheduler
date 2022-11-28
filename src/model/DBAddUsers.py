import sqlite3
import Constants as C

# Adds new clients and drivers to the database
def AddUsers():
    conn = sqlite3.connect(C.DBPATH)
    c = conn.cursor()

    loop = True
    while loop == True:
        choice = input("1: add client, 2: add driver, 3: finished ")
        if choice == '1':
            fName = input("enter client first name: ")
            lName = input("enter client last name: ")
            lat = input("enter client lattitude: ")
            long = input("enter client longitude: ")
            entry = [lName, fName, lat, long]
            c.execute('INSERT INTO clients VALUES (?,?,?,?)', entry)
        elif choice == '2':
            fName = input("enter driver first name: ")
            lName = input("enter driver last name: ")
            lat = input("enter driver lattitude: ")
            long = input("enter driver longitude: ")
            entry = [lName, fName, lat, long]
            c.execute('INSERT INTO drivers VALUES (?,?,?,?)', entry)
        elif choice == '3':
            loop = False
            print("Session completed")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    AddUsers()