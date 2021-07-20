from . import getArgs
from . import getMemoryUsage
from . import getCpuUsage
from . import getUptime
from . import pingHost
from . import GB

from time import sleep
import csv

def singleLoop(args):
    """Performs a single monitoring loop
    Monitors:
        Memory
        CPU
        Uptime
        Pings a single host
    """
    pingResult = pingHost(args.host)
    mem = getMemoryUsage()
    cpuPercent = getCpuUsage()
    uptime = getUptime()

    if args.debug > 0:
        print("[+] Memory Usage:", mem)
        print("[+] CPU Usage (%):", cpuPercent)
        print("[+] Time Stats:", uptime)
        print(f"[+] Ping {args.host}:", pingResult)

    return {**pingResult, **mem, **cpuPercent, **uptime}

def primaryLoop(args):
    #Primes CPU value and retrieves Headers for CSV File
    loopResult = singleLoop(args)

    with open(args.outfile, 'w') as f:
        try:
            w = csv.DictWriter(f, loopResult.keys())
            w.writeheader()
            while True:
                loopResult = singleLoop(args)
                print(loopResult)
                w.writerow(loopResult)
                sleep(args.wait)
        except(KeyboardInterrupt):
            f.close()
            raise

def main():
    args = getArgs()
    print("[+] Gathering System Information")

    try:
        primaryLoop(args)
    except(KeyboardInterrupt):
        exit()
