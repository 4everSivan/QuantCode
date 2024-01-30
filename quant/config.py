import sys
import yaml

from typing import Dict, Any, Optional
from .tools import Tools


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

    def initialize(self) -> None:
        if not self.config.get('general'):
            print(
                "Config error: General section is missing",
                flush=True,
                file=sys.stderr
            )
            sys.exit(1)

        if not self.config['general'].get('target'):
            print(
                "Config error: general section params target is missing",
                flush=True,
                file=sys.stderr
            )
            sys.exit(1)

        check_res = Tools.check_path(self.config['general']['target'], tp="dir")
        if not check_res.get('state'):
            print(
                check_res.get('err_msg'),
                flush=True,
                file=sys.stderr
            )
            sys.exit(1)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.config.get(key, default)

    def keys(self) -> Any:
        return self.config.keys()

    def __contains__(self, key: str) -> bool:
        return key in self.config

    def __getitem__(self, key: str) -> Any:
        return self.config[key]
