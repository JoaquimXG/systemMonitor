from . import datastream

from time import sleep
import os

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
