from . import datastream

from time import sleep
import os


def showInfo(args, func):
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            infoString = func(args, datastream)
            print(f"{infoString}\n\n\nPress Ctrl-C to return to menu")
            sleep(args["wait"])
    except (KeyboardInterrupt):
        return


def getMostRecentInfo(datastream):
    mostRecentInfo = {}
    while True:
        try:
            mostRecentInfo = datastream[-1]
            break
        except (IndexError):
            sleep(0.1)

    return mostRecentInfo


def getUptimeInfo(args, datastream):
    mostRecentInfo = getMostRecentInfo(datastream)
    uptime = mostRecentInfo["Uptime"]
    bootTime = mostRecentInfo["Boot Time"]
    return f"System Uptime Information:\n\nUptime: {uptime}\tBoot Time: {bootTime}"


def getMemoryInfo(args, datastream):
    mostRecentInfo = getMostRecentInfo(datastream)
    total = mostRecentInfo["Total Memory"]
    available = mostRecentInfo["Available Memory"]
    usedPercentage = mostRecentInfo["Percentage Memory Used"]
    availablePercentage = mostRecentInfo["Percentage Memory Available"]
    return f"Current Memory Usage:\n\nUsed (%): {usedPercentage}\tAvailable (%): {availablePercentage}\tAvailable (GB): {available}\tTotal (GB): {total}"


def getCpuInfo(args, datastream):
    mostRecentInfo = getMostRecentInfo(datastream)
    used = mostRecentInfo["Percentage CPU Used"]
    return f"Current CPU Usage (%): {used}"


def getPingMonitorInfo(args, datastream):
    mostRecentInfo = getMostRecentInfo(datastream)
    host = mostRecentInfo["Ping Hostname"]
    isUp = mostRecentInfo["Ping Host is Online"]

    count = 0
    onlineCount = 0
    for record in datastream[::-1]:
        if record["Ping Host is Online"]:
            onlineCount += 1
        count += 1

    uptimePercent = onlineCount / count * 100

    return f"Ping Monitor for {host}:\n\nHost is online: {isUp}\tHost Response Percentage (last {count*args['wait']}s): {uptimePercent}"


def getSiteInfo(args, datastream):
    mostRecentInfo = getMostRecentInfo(datastream)
    host = mostRecentInfo["Site Monitor Hostname"]
    isUp = mostRecentInfo["Site is Online"]
    statusCode = mostRecentInfo["Site Monitor HTTP Status Code"]

    count = 0
    onlineCount = 0
    for record in datastream[::-1]:
        if record["Site is Online"]:
            onlineCount += 1
        count += 1

    uptimePercent = onlineCount / count * 100

    return f"Site Monitor for {host}:\n\nSite is online: {isUp}\tStatus Code: {statusCode}\tSuccess code Response Percentage (last {count*args['wait']}s): {uptimePercent}"
