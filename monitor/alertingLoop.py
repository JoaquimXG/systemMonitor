from . import alerts, datastream
from . import getMemoryUsage

from time import sleep

def cpuAlert():
    if datastream[-1]['Percentage CPU Used'] > 75:
        alerts['cpuGreaterThan75'] = True
    else:
        alerts['cpuGreaterThan75'] = False

def pingAlert():
    limit = 10
    count = 0
    onlineCount = 0
    for i, record in enumerate(datastream[::-1]):
        if record["Ping Host is Online"]:
            onlineCount += 1
        count += 1
        if i == limit:
            break

    uptimePercent = onlineCount / count * 100

    if uptimePercent < 50:
        alerts['pingMonitorOffline'] = True
    else:
        alerts['pingMonitorOffline'] = False


def alertingLoop(args):
    while True:
        try:
            cpuAlert()
            pingAlert()
        except(IndexError):
            sleep(0.5)

        sleep(args['wait'])
