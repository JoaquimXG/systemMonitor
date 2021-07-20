import argparse
from .version import version

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

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=version()),
    )
    args = parser.parse_args()

    return args
