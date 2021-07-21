from . import getMemoryUsage
from . import getCpuUsage
from . import getUptime
from . import pingHost
from . import GB
from . import AsyncWrite
from . import datastream

from time import sleep
from collections import OrderedDict
from datetime import datetime
import csv

def singleLoop(args):
    """Performs a single monitoring loop
    Monitors:
        Memory
        CPU
        Uptime
        Pings a single host
    """
    def dictToTuples(dict):
        return [(k, v) for k, v in dict.items()]

    pingResult = pingHost(args["host"])
    mem = getMemoryUsage()
    cpuPercent = getCpuUsage()
    uptime = getUptime()

    if args["debug"] > 0:
        print("[+] Memory Usage:", mem)
        print("[+] CPU Usage (%):", cpuPercent)
        print("[+] Time Stats:", uptime)
        print(f"[+] Ping {args['host']}:", pingResult)

    return OrderedDict(
        [
            ("Timestamp", datetime.now().strftime("%H:%M:%S-%m/%d/%y")),
            *dictToTuples(pingResult),
            *dictToTuples(mem),
            *dictToTuples(cpuPercent),
            *dictToTuples(uptime),
        ]
    )

def monitoringLoop(args):
    # Primes CPU value and retrieves Headers for CSV File
    loopResult = singleLoop(args)

    try:
        with open(args["outfile"], "w", newline="") as f:
            w = csv.DictWriter(f, loopResult.keys())
            w.writeheader()
    except(KeyboardInterrupt):
        raise

    while True:
        loopResult = singleLoop(args)
        datastream.append(loopResult)
        if len(datastream) > 10:
            datastream.pop(0)
        background = AsyncWrite.AsyncWrite(loopResult, args['outfile'])
        background.start()
        if args["debug"] > 0:
            print("[+] Writing to file", loopResult)
        sleep(args["wait"])
