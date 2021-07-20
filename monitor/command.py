from . import getArgs
from . import getMemoryUsage
from . import getCpuUsage
from . import getUptime
from . import pingHost
from . import GB

def singleLoop(args):
    """Performs a single monitoring loop
    Monitors:
        Memory
        CPU
        Uptime
        Pings a single host
    """
    mem = getMemoryUsage()
    cpuPercent = getCpuUsage()
    uptime = getUptime()
    pingResult = pingHost(args.host)

    if args.debug > 0:
        print("Memory Usage:", mem)
        print("CPU Usage (%):", cpuPercent)
        print("Time Stats:", uptime)
        print(f"Ping {args.host}:", pingResult)

    return {"memUsage": mem,
            "cpuUsage": cpuPercent,
            "uptime": uptime,
            "ping": pingResult}

def main():
    args = getArgs()
    loopResult = singleLoop(args)

    print(loopResult)
