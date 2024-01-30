import sys
import yaml

from typing import Dict

class Config:

    def __init__(self, path: str) -> None:
        self.config = self.read_config(path)

    @staticmethod
    def read_config(path: str) -> Dict:
        try:
            if path.endswith('.yml') or path.endswith('.yaml'):
                with open(path) as f:
                    config = yaml.load(f, Loader=yaml.FullLoader)
                    return config
            else:
                print(
                    "Config error: Unknown file type {}".format(path),
                    flush=True,
                    file=sys.stderr
                )
                sys.exit(1)
        except Exception as e:
            err_msg = 'Config error: Config file "{}" load failed: {}'.format(path, e)
            print(
                err_msg,
                flush=True,
                file=sys.stderr
            )
            sys.exit(1)
