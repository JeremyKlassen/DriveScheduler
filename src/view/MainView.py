def MainView():
    menuOption = input("1: make list , 2: to add/remove people from database, 3: to initialize Database, 4: to update distances/times")
    return menuOption

if __name__ == '__main__':
    print(MainView())