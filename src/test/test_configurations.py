import unittest
import pytest
from ..driveckup.config import config, default_config
from yaml import load, CLoader


@pytest.mark.skip
def test_foo():
    assert False


class TestConfig(unittest.TestCase):
    def test_config_is_default(self):
        assert config == default_config

    def test_config(self):
        f = open(default_config['driveckup']['config_file'])
        cfg = load(f, Loader=CLoader)
        print(type(cfg))
        print(cfg)
        self.assertIsInstance(cfg, dict)
        self.assertDictEqual(default_config, cfg)
