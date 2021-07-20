import psutil
from .memsizes import GB

def getMemoryUsage():
    """Gets the total, available and percentage utilise"""
    mem = psutil.virtual_memory()._asdict()

    returnMem = {}
    returnMem['total'] = round(mem['total']/GB, 2)
    returnMem['available'] = round(mem['available']/GB, 2)
    returnMem['percentUsed'] = mem['percent']
    returnMem['percentAvailable'] = 100 - mem['percent']

    return returnMem
