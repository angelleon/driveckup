from pathlib import Path
from random import choice
from argparse import ArgumentParser
from mk_file import mk_file, charset, gen_name, FILE_SIZE, NAME_LENGTH


def mk_dir(root, dir_count, file_count, file_size, binary, level):
    if level == 0:
        return
    root = Path(root)
    name = gen_name()
    new_dir = root / name
    new_dir.mkdir()
    for _ in range(file_count):
        mk_file(new_dir, file_size, binary)
    for _ in range(dir_count):
        mk_dir(new_dir, dir_count, file_count, file_size, binary, level - 1)


def main():
    parser = ArgumentParser()
    parser.add_argument('-f', '--files', type=int, default=2)
    parser.add_argument('-d', '--directories', type=int, default=2)
    parser.add_argument('-s', '--size', type=int, default=FILE_SIZE)
    parser.add_argument('-l', '--levels', type=int, default=2)
    parser.add_argument('-r', '--root', default='.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b', '--binary', default=False)
    group.add_argument('-t', '--text', default=True)
    args = parser.parse_args()
    file_count = args.files
    dir_count = args.directories
    file_size = args.size
    levels = args.levels
    root_dir = args.root
    binary = args.binary and not args.text
    mk_dir(root_dir, dir_count, file_count, file_size, binary, levels)


if __name__ == '__main__':
    main()
