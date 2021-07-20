from datetime import datetime
import psutil
from ping3 import ping
from .memsizes import GB

def getMemoryUsage():
    """Gets the total and available memory"""
    mem = psutil.virtual_memory()._asdict()

    returnMem = {}
    returnMem['Total Memory'] = round(mem['total']/GB, 2)
    returnMem['Available Memory'] = round(mem['available']/GB, 2)
    returnMem['Percentage Memory Used'] = mem['percent']
    returnMem['Percentage Memory Available'] = round(100 - mem['percent'], 1)

    return returnMem

def getCpuUsage():
    """Gets CPU usage since previous call"""
    cpuPercent = psutil.cpu_percent(0.2)
    return {"Percentage CPU Used": cpuPercent}

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


    return {"Uptime": uptime, "Boot Time": bootTime}

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
    
    return {'Ping Hostname': host, 'Ping Host is Online': res}
