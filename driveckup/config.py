from typing import Union
from utils import FileRepo

import yaml
from pathlib import Path


__f_repo = None


def parse_config(path: Union[Path, str], file_repo: FileRepo) -> dict:
    with file_repo.get(path) as f:
        return yaml.load(f, Loader=yaml.CLoader)


default_config = {
    'driveckup': {
        'workers_count': 5,
        'credentials_path': './credentials.json',
        'config_file': './driveckup.yaml',
        'hostname': 'localhost',
        'port': 3757,  # drkp
    }
}

config = default_config

if __f_repo is None:
    from utils import FileRepo
    __f_repo = FileRepo()

with __f_repo.open(default_config['driveckup']['config_file']) as f:
    config = yaml.load(f, Loader=yaml.CLoader)

daemon_conf = {}
worker_conf = {}
