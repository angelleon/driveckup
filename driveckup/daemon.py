from multiprocessing import Semaphore, Queue, Process, Event
# from time import sleep
from pathlib import Path
from .driveckup import Driveckup


class Worker(Process):
    def __init__(self, queue: Queue, config, path: Path, drive: Driveckup,
                 sem: Semaphore, finish_ev: Event):
        super().__init__()
        self.config = config
        self.path = path
        self.drive = drive
        self.sem = sem
        self.queue = queue
        self.finish_ev = finish_ev

    def run(self):
        while not self.finish_ev.is_set():
            backup_info: tuple = self.queue.get(
                block=True, timeout=self.config['timeout'])
            if backup_info is None:
                continue
            path: Path
            parent_id: str
            path = backup_info[0]
            parent_id = backup_info[1]
            if path.is_dir():
                self.drive.backup_directory(path)
            if path.is_file():
                self.drive.backup_file(path)


class Daemon:
    def __init__(self, conf: dict, worker_conf: dict, drkp: Driveckup, queue: Queue):
        self._conf = conf
        self._queue = queue
        self._worker_conf = worker_conf
        self._drkp = drkp
        self._workers = [Worker() for _ in range(conf['max_works']()]

    def start(self):
        pass
