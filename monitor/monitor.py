import psutil
from .memsizes import GB

def getMemoryUsage():
    """Gets the total and available memory"""
    mem = psutil.virtual_memory()._asdict()

    returnMem = {}
    returnMem['total'] = round(mem['total']/GB, 2)
    returnMem['available'] = round(mem['available']/GB, 2)
    returnMem['percentUsed'] = mem['percent']
    returnMem['percentAvailable'] = 100 - mem['percent']

    return returnMem

def getCpuUsage():
    """Gets CPU usage percentage from the prior 1 second"""
    cpuPercent = psutil.cpu_percent(1)
    return cpuPercent
