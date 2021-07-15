

from argparse import ArgumentParser
from driveckup.driveckup import Driveckup
from driveckup.file_repo import LocalFileRepo


def main():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', default=None)
    group.add_argument('-d', '--directory', default=None)
    parser.add_argument('-p', '--dest-path', default=None)
    args = parser.parse_args()
    f = args.file
    d = args.directory
    dest_path = args.dest_path
    file_repo = LocalFileRepo()
    driveckup = Driveckup(file_repo)
    if f is not None:
        driveckup.backup_file(f)
    if d is not None:
        driveckup.backup_directory(d)
    print('Success')



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExitting...')