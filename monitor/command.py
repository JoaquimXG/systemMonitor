from . import monitoringLoop
from . import getArgs
from . import menu

from time import sleep
import threading

def main():
    args = vars(getArgs())
    monitoringThread = threading.Thread(target=monitoringLoop, daemon=True, args=(args,))
    monitoringThread.start()

    try:
        menu(args)
    except(KeyboardInterrupt):
        exit()
