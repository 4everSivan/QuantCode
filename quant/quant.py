import argparse
import multiprocessing
import os
import sys

from . import BANNER
from .config import Config


def worker(
        p_id: int,
        config: Config,
        m_event: multiprocessing.Event,
        m_queue: multiprocessing.JoinableQueue
) -> None:
    pass


def run(config: Config) -> None:
    # get target dir
    all_dir = os.listdir(config['general'].get('target'))

    for item in all_dir[:]:
        if '.' in item:
            all_dir.remove(item)

    processes = []
    event = multiprocessing.Event()
    join_queue = multiprocessing.JoinableQueue()

    for i in range(len(all_dir)):
        processes.append(
            multiprocessing.Process(
                target=worker,
                args=(i, config, event, join_queue)
            )
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="QuantCode: statistics code and graphical display. ")
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

    args = parser.parse_args()

    if args.version:
        print(BANNER, flush=True)
        sys.exit(0)

    config_path = args.config

    if not config_path:
        parser.parse_args(['-h'])
        sys.exit(0)

    config = Config(config_path)
    config.initialize()

    run(config)