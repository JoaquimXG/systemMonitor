from . import datastream

from time import sleep
import os

def showMemoryInfo(args):
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            mostRecentInfo = datastream[-1]
            total = mostRecentInfo['Total Memory']
            available = mostRecentInfo['Available Memory']
            usedPercentage = mostRecentInfo['Percentage Memory Used']
            availablePercentage = mostRecentInfo['Percentage Memory Available']
            print(f"Current Memory Usage:\nUsed (%): {usedPercentage}\tAvailable (%): {availablePercentage}\tAvailable (GB): {available}\tTotal (GB): {total}\n\n\nPress Ctrl-C to return to menu")
            sleep(args['wait'])
    except(KeyboardInterrupt):
        return


def showCpuInfo(args):
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            mostRecentInfo = datastream[-1]
            used = mostRecentInfo['Percentage CPU Used']
            print(f"Current CPU Usage (%): {used}\n\n\nPress Ctrl-C to return to menu")
            sleep(args['wait'])
    except(KeyboardInterrupt):
        return
