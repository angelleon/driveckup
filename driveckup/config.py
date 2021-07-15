import yaml
from pathlib import Path
from stat import S_IRUSR

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

__f = Path(default_config['driveckup']['config_file'])
if __f.exists() \
        and __f.is_file() \
        and __f.stat().st_mode & S_IRUSR:
    config = yaml.load(__f.open(), Loader=yaml.CLoader)
