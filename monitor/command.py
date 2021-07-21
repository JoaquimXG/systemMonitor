from . import monitoringLoop
from . import getArgs
from . import menu

from time import sleep
import threading

def main():
    args = vars(getArgs())
    x = threading.Thread(target=monitoringLoop, daemon=True, args=(args,))
    x.start()

    try:
        menu()
    except(KeyboardInterrupt):
        exit()
