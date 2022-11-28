import sqlite3
import Constants as C

# Adds new clients and drivers to the database
def AddUsers():
    conn = sqlite3.connect(C.DBPATH)
    c = conn.cursor()

    loop = True
    while loop:
        choice = input ("1: add client, 2: add driver, 3: finished")
        if choice == 1:
            print("add client")
        if choice == 2:
            print("add driver")
        if choice == 3:
            loop == False


if __name__ == __main__:
    AddUsers()