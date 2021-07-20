from . import getMemoryUsage
from . import getCpuUsage
from . import GB

def main():
    mem = getMemoryUsage()
    print("Memory Usage:", mem)

    cpuPercent = getCpuUsage
    print("CPU Usage (%):", cpuPercent())
