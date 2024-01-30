import argparse
import sys

from . import BANNER


def main() -> None:
    parser = argparse.ArgumentParser(description="QuantCode: statistics code number and graphical display. ")
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        dest='config',
        help="Path to the QuantCode configuration file. "
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="QuantCode version"
    )

    args =  parser.parse_args()

    if args.version:
        print(BANNER, flush=True)
        sys.exit(0)

    config_path = args.config

    if not config_path:
        parser.parse_args(['-h'])
        sys.exit(0)

