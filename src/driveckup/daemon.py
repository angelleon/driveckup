from multiprocessing import Semaphore, Queue, Process, Event
from time import sleep
from pathlib import Path
from .driveckup import Driveckup
from .db_repo import DrkpDB


class Listener(Process):
    def __init__(self, queue: Queue, stop_ev: Event):
        self._queue = queue
        self._stop_ev = stop_ev

    def run(self):
        while not self._stop_ev.is_set():
            sleep(2)


class Loader(Process):
    pass


class Worker(Process):
    def __init__(self, queue: Queue, config, drive: Driveckup,
                 sem: Semaphore, finish_ev: Event):
        super().__init__()
        self.config = config
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
            if path.is_symlink():
                self.drive.backup_symlink(path)


class Daemon:
    def __init__(self, conf: dict, worker_conf: dict, drkp: Driveckup,
                 queue: Queue, db_repo: DrkpDB):
        self._conf = conf
        self._queue = queue
        self._worker_conf = worker_conf
        self._drkp = drkp
        self._db_repo = db_repo
        path = None
        self._sem = Semaphore()
        self._stop_ev = Event()
        self._workers = [Worker(queue, worker_conf, path, drkp,
                                self._sem, self._stop_ev)
                         for _ in range(conf['max_works'])]

    def start(self):
        self._db_repo.open()
        for w in self._workers:
            w.start()
        for w in self._workers:
            w.join()
