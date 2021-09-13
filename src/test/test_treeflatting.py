import pytest
from pathlib import Path
from unittest import TestCase
from time import sleep

from ..driveckup.file_repo import PosixFSNode


class TestTreeflatting(TestCase):
    def test_comparsion(self):
        node = PosixFSNode(Path('eggs'))
        expected_node = PosixFSNode(Path('eggs'))
        path = Path('eggs')
        assert node == path
        assert node == expected_node
        assert (node == 0) is False

    def test_iterator(self):
        node = PosixFSNode(Path('eggs'))
        for item in node:
            print(item)
            # print(next(item))
            assert isinstance(item, PosixFSNode)

    def test_treeflattings(self):
        node = PosixFSNode(Path('eggs'))
        content = [item for item in node]
        expected = list(map(lambda p: PosixFSNode(Path(p)), ('eggs', 'eggs/eggs',
                                                             'eggs/eggs/foo', 'eggs/eggs/spam', 'eggs/foo', 'eggs/spam')))
        print(expected)
        print(content)
        self.assertListEqual(expected, content)
