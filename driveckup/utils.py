from pathlib import Path
from stat import S_IRUSR
from typing import Union
from io import TextIOWrapper
from pwd import getpwuid
from os import getuid


class FileRepo:
    def __init__(self):
        pass

    def __convert_path(self, path):
        if not isinstance(path, (str, Path)):
            raise TypeError("path must be a str or a Path object")
        if isinstance(path, str):
            path = Path(path)
        return path

    def __chk_file(self, path: Path):
        if not path.exists():
            raise FileNotFoundError(
                f'The specified path [{str(path)}] does not exist')
        if not path.is_file():
            raise FileNotFoundError('Specified path [{str(path)}] is not a file')
        if not path.stat().st_mode & S_IRUSR:
            username = getpwuid(getuid())[0]
            raise PermissionError(
                f'Read acces is not allowed for user [{username}] on file [{str(path)}]')

    def open(self, path: Union[str, Path]) -> TextIOWrapper:
        path = self.__convert_path(path)
        self.__chk_file(path)
        return path.open()
