from datetime import datetime
import psutil
from ping3 import ping
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

def getUptime():
    """Gets the time since last reboot"""

    def convertTimedeltaToString(timedelta):
        timedelta = timedelta.total_seconds()
        hours, remainder = divmod(timedelta, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

    bootTime = psutil.boot_time()
    bootTime = datetime.fromtimestamp(bootTime)
    uptime = datetime.now() - bootTime
    uptime = convertTimedeltaToString(uptime)

    bootTime = bootTime.strftime("%H:%M:%S")


    return {"uptime": uptime, "boot": bootTime}

def pingHost(host):
    """Pings a host
    Returns: 
        True if host is up
        False if host is host is unknown (no ip address found)
        None if no response from host (host is down)
    """
    res = ping(host)
    if type(res) == float:
        res = True
    
    return res
