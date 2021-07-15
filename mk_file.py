from pathlib import Path
from random import choice, randint
from string import ascii_letters, digits
from argparse import ArgumentParser

FILE_SIZE = 2 * 1024
WRITE_BLOCK_SIZE = 4 * 1024
NAME_LENGTH = 6
charset = ascii_letters + digits


def gen_name():
    return gen_text(NAME_LENGTH)


def gen_bin(length):
    return b''.join(randint(0, 255) for _ in range(length))


def gen_text(length):
    return ''.join(choice(charset) for _ in range(length))


def mk_file(directory: Path, file_size, binary=False):
    name = gen_name()
    new_file = directory / name

    if binary:
        generator = gen_bin
        mode = 'wb'
    else:
        generator = gen_text
        mode = 'w'
    f = new_file.open(mode)
    block_count = file_size // WRITE_BLOCK_SIZE
    tail = file_size % WRITE_BLOCK_SIZE
    i = 0
    while i < block_count:
        f.write(generator(WRITE_BLOCK_SIZE))
        i += 1
    if tail > 0:
        f.write(generator(tail))
    f.close()


def main():
    parser = ArgumentParser()
    parser.add_argument('-f', '--files', default=2)
    parser.add_argument('-s', '--size', default=FILE_SIZE)
    parser.add_argument('-r', '--root', default='.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b', '--binary', default=False)
    group.add_argument('-t', '--text', default=True)
    args = parser.parse_args()
    file_size = args.size
    root_dir = args.root
    binary = args.binary and not args.text
    mk_file(root_dir, file_size, binary)




if __name__ == '__main__':
    main()
