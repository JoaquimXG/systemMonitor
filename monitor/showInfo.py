from . import datastream

from time import sleep
import os

def showInfo(args, func):
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            mostRecentInfo = datastream[-1]
            infoString = func(mostRecentInfo)
            print(f"{infoString}\n\n\nPress Ctrl-C to return to menu")
            sleep(args['wait'])
    except(KeyboardInterrupt):
        return

def getUptimeInfo(mostRecentInfo):
    uptime = mostRecentInfo['Uptime']
    bootTime = mostRecentInfo['Boot Time']
    return f"System Uptime Information:\nUptime: {uptime}\tBoot Time: {bootTime}"

def getMemoryInfo(mostRecentInfo):
    total = mostRecentInfo['Total Memory']
    available = mostRecentInfo['Available Memory']
    usedPercentage = mostRecentInfo['Percentage Memory Used']
    availablePercentage = mostRecentInfo['Percentage Memory Available']
    return f"Current Memory Usage:\nUsed (%): {usedPercentage}\tAvailable (%): {availablePercentage}\tAvailable (GB): {available}\tTotal (GB): {total}"

def getCpuInfo(mostRecentInfo):
    used = mostRecentInfo['Percentage CPU Used']
    return f"Current CPU Usage (%): {used}"
