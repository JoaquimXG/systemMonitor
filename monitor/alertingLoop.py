from . import alerts, datastream
from . import getMemoryUsage

from time import sleep

def alertingLoop(args):
    while True:
        try:
            if datastream[-1]['Percentage CPU Used'] > 75:
                alerts['cpuGreaterThan75'] = True
            else:
                alerts['cpuGreaterThan75'] = False
        except(IndexError):
            sleep(0.5)

        sleep(args['wait'])
