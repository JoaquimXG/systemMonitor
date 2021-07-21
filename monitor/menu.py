import os

def printMenu(title, options):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(30 * "-" , title , 30 * "-") 
    exit = 1
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
        exit += 1

    print(f"{exit}. Exit")
    print(76 * "-")

def menu():
    prompt = "Enter your choice: "
    while True:
        printMenu("System Monitor", ["Uptime", "Memory Usage", "CPU Usage", "Ping Success Rate"])
        choice = input(prompt)
         
        if choice == '1':     
            break
        elif choice == '2':
            break
        elif choice == '3':
            break
        elif choice == '4':
            break
        elif choice == '5':
            menu()
        else: 
            prompt = "Option not available. Enter another choice: "
