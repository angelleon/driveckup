from driveckup.driveckup import Driveckup
from driveckup.daemon import Daemon
from driveckup.utils import FileRepo
from driveckup.config import config, daemon_conf, worker_conf
from multiprocessing import Queue, Event


def main():
    drkp = Driveckup(FileRepo())
    daemon = Daemon(daemon_conf, worker_conf)
    daemon.start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Process finished by user')
