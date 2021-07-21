from . import datastream

from time import sleep
import os

def showInfo(args, func):
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            infoString = func(args, datastream)
            print(f"{infoString}\n\n\nPress Ctrl-C to return to menu")
            sleep(args['wait'])
    except(KeyboardInterrupt):
        return

def getUptimeInfo(args, datastream):
    mostRecentInfo = datastream[-1]
    uptime = mostRecentInfo['Uptime']
    bootTime = mostRecentInfo['Boot Time']
    return f"System Uptime Information:\nUptime: {uptime}\tBoot Time: {bootTime}"

def getMemoryInfo(args, datastream):
    mostRecentInfo = datastream[-1]
    total = mostRecentInfo['Total Memory']
    available = mostRecentInfo['Available Memory']
    usedPercentage = mostRecentInfo['Percentage Memory Used']
    availablePercentage = mostRecentInfo['Percentage Memory Available']
    return f"Current Memory Usage:\nUsed (%): {usedPercentage}\tAvailable (%): {availablePercentage}\tAvailable (GB): {available}\tTotal (GB): {total}"

def getCpuInfo(args, datastream):
    mostRecentInfo = datastream[-1]
    used = mostRecentInfo['Percentage CPU Used']
    return f"Current CPU Usage (%): {used}"

def getPingMonitorInfo(args, datastream):
    mostRecentInfo = datastream[-1]
    host = mostRecentInfo['Ping Hostname']
    isUp = mostRecentInfo['Ping Host is Online']

    count = 0
    onlineCount = 0
    for record in datastream[::-1]:
        if record['Ping Host is Online']:
            onlineCount += 1
        count += 1
    
    uptimePercent = onlineCount/count * 100

    return f"Ping Monitor for {host}:\nHost is online: {isUp}\tHost Response Percentage (last {count*args['wait']}s): {uptimePercent}"

