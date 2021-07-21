def printMenu():
    print(30 * "-" , "MENU" , 30 * "-") 
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("3. Menu Option 3")
    print("4. Menu Option 4")
    print("5. Exit")
    print(67 * "-")

def menu():
    while True:
        printMenu()
        choice = input("Enter your choice [1-5]: ")
         
        if choice==1:     
            print("Menu 1 has been selected")
        elif choice==2:
            print("Menu 2 has been selected")
        elif choice==3:
            print("Menu 3 has been selected")
        elif choice==4:
            print("Menu 4 has been selected")
        elif choice==5:
            print("Menu 5 has been selected")
            loop=False
        else:
            print("Wrong option selection. Enter any key to try again..")
