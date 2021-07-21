import argparse
from .version import __version__

def getArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbosity (-v, -vv, etc)"
    )

    parser.add_argument(
        "-d", "--debug", dest="debug", action="store_true", default=False, help="Displays debugging information"
    )

    parser.add_argument(
        "-t",
        "--target-host",
        action="store",
        dest="host",
        default="tlagranite.co.uk",
        help="Target host for ping monitor",
    )

    parser.add_argument(
        "-w",
        "--wait",
        action="store",
        type=int,
        dest="wait",
        default="5",
        help="Time to wait between monitoring loops in (s)",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        action="store",
        dest="outfile",
        default="systemMonitor.csv",
        help="Output CSV file for loggin",
    )

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__),
    )
    args = parser.parse_args()

    return args
