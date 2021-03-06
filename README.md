# SystemMonitor

Created on request for a client to monitor some basic but specific information on a collection of servers. 

## Metrics

- CPU utilisation 
- Memory utilisation
- Uptime for a remote host
- HTTP response for a remote host

Outputs metric to terminal and optionally logs to a file. 

## Requirements

- Python 3.5
- psutil
- ping3
- requests

## Usage

```bash
usage: monitor [-h] [-v] [-d] [-t HOST] [-w WAIT] [-o OUTFILE] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Verbosity (-v, -vv, etc)
  -d, --debug           Displays debugging information
  -t HOST, --target-host HOST
                        Target host for ping monitor
  -w WAIT, --wait WAIT  Time to wait between monitoring loops in (s)
  -o OUTFILE, --outfile OUTFILE
                        Output CSV file for logging
  --version             show program's version number and exit
```
