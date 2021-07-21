from . import showCpuInfo

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

def menu(args):
    prompt = "Enter your choice: "
    while True:
        printMenu("System Monitor", ["Uptime", "Memory Usage", "CPU Usage", "Ping Success Rate"])
        choice = input(prompt)
         
        if choice == '1':     
            showCpuInfo(args)
        elif choice == '2':
            showCpuInfo(args)
        elif choice == '3':
            showCpuInfo(args)
        elif choice == '4':
            showCpuInfo(args)
        elif choice == '5':
            exit()
        else: 
            prompt = "Option not available. Enter another choice: "
