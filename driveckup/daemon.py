from multiprocessing import Semaphore, Queue, Process, Pool, Event
# from time import sleep
from config import DaemonConf, WorkerConf
from pathlib import Path
from .driveckup import Driveckup


class Worker(Process):
    def __init__(self, queue: Queue, config, path: Path, drive: Driveckup,
                 sem: Semaphore, finish_ev: Event):
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
    def __init__(self, conf: DaemonConf, queue: Queue, w_conf: WorkerConf):
        self._conf = conf
        self._pool = Pool(conf['max_works'])
        self._queue = queue
        self._w_conf = w_conf
