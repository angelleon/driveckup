import sqlite3
from file_repo import FileRepo
from pathlib import Path


class DrkpDB:
    def __init__(self, config: dict, file_repo: FileRepo):
        pass

    def create(self, file_repo: FileRepo):
        pass

    def open(self):
        pass

    def insert(self, path: Path):
        pass

    def select(self, path: Path):
        pass

    def update(self, path: Path):
        pass

    def delete(self, path: Path):
        pass


class SQLiteDB(DrkpDB):
    def __init__(self, config: dict, file_repo: FileRepo):
        self.config = config
        self.f_repo = file_repo
        self._db = sqlite3.connect(**config.connection)

    def create(self, file_repo: FileRepo):
        self.config['model_path']
        model_files = file_repo.get_dir_files()
        for f in model_files:
            f = f.open()
            sentences = f.read()
            self._db.executemany(sentences)

    def open(self):
        pass

    def insert(self, path: Path):
        pass

    def select(self, path: Path):
        pass

    def update(self, path: Path):
        pass

    def delete(self, path: Path):
        pass
