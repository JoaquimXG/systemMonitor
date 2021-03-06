from . import showInfo, getUptimeInfo, getMemoryInfo, getCpuInfo, getPingMonitorInfo, getSiteInfo

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
        printMenu("System Monitor", ["Uptime", "Memory Usage", "CPU Usage", "Ping Monitor", "Website Monitor"])
        choice = input(prompt)
         
        if choice == '1':     
            showInfo(args, getUptimeInfo)
        elif choice == '2':
            showInfo(args, getMemoryInfo)
        elif choice == '3':
            showInfo(args, getCpuInfo)
        elif choice == '4':
            showInfo(args, getPingMonitorInfo)
        elif choice == '5':
            showInfo(args, getSiteInfo)
        elif choice == '6':
            exit()
        else: 
            prompt = "Option not available. Enter another choice: "
