from . import getMemoryUsage
from . import getCpuUsage
from . import getUptime
from . import GB

def main():
    mem = getMemoryUsage()
    print("Memory Usage:", mem)

    cpuPercent = getCpuUsage
    print("CPU Usage (%):", cpuPercent())

    uptime = getUptime()
    print("Time Stats:", uptime)
