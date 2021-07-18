from unittest import TestCase
from multiprocessing import Process
from ..driveckup.driveckup import Driveckup
from pathlib import Path
from time import sleep
from ..driveckup.file_repo import LocalFileRepo as FileRepo

'''from ..mk_dir import mk_dir'''


class Uploader(Process):
    def __init__(self, drkp: Driveckup, path: Path):
        super().__init__()
        self._drkp = drkp
        self._path = path

    def run(self):
        print(self._path)
        if self._path.is_file():
            self._drkp.backup_file(self._path)
        if self._path.is_dir():
            self._drkp.backup_directory(self._path)
        sleep(3)


class TestMultiupload(TestCase):
    def test_multiupload(self):
        drkp = Driveckup(FileRepo(), './eggs/spam')
        u1 = Uploader(drkp, Path('./eggs/spam'))
        u2 = Uploader(drkp, Path('./eggs/foo'))
        u1.start()
        u2.start()
        u1.join()
        u2.join()
        assert False

