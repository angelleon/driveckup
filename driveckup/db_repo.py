import sqlite3
from config import DBConfig
from file_repo import FileRepo


class DrkpDB:
    def __init__(self, config: DBConfig, file_repo: FileRepo):
        self.config = config
        self.f_repo = f_repo
        self._db = sqlite3.connect(**config.connection)

    def create(self, file_repo: FileRepo):
        self.config['model_path']
        model_files = file_repo.get_dir_files()
        for f in model_files:
            f = f.open()
            sentences = f.read()
            self._db.executemany(sentences)

    def open(self):
        db_file =
