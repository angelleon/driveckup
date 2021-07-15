from pathlib import Path
from io import FileIO
from typing import Union


class FileRepo:
    def get(self, f_path: Union[str, Path]) -> Path:
        pass


class LocalFileRepo(FileRepo):
    def get(self, f_path: Union[str, Path]) -> FileIO:
        f_path = Path(f_path)
        if not f_path.exists():
            raise ValueError(f'File not found [{f_path}]')
        if not f_path.is_file():
            raise ValueError(f'[{f_path}] is not a file')
        return f_path

    def get_dir(self, d_path):
        if not isinstance(d_path, (str, Path)):
            raise ValueError(f'Provided path [{d_path}] is not str nor Path')
        if isinstance(d_path, str):
            d_path = Path(d_path)
        if not d_path.exists():
            raise ValueError(f'[{d_path}] does not exist')
        if not d_path.is_dir():
            raise ValueError(f'[{d_path}] is not a directory')
        return d_path

    def get_dir_cont(self, d_path: Union[str, Path]) -> Path:
        d_path = self.get_dir(d_path)
        content = [child for child in d_path.iterdir() if (child.is_file() or child.is_dir())]
        return content
