import unittest
import os
from yamlsub.config import Config

class TestConfig(unittest.TestCase):

    def test_config(self):
        # path valid when runnint test from top level directory
        env_path = os.path.join(os.getcwd(), 'tests', 'resources', '.env')
        yaml_path = os.path.join(os.getcwd(), 'tests', 'resources', 'test-config.yaml')

        cfg = Config(yaml_path=yaml_path, env_path=env_path)

        self.assertIsNotNone(cfg.get_config())
        key2 = cfg.get_config_key('auth_keys')['key2']
        self.assertEqual(key2, 'env_test_key2')

if __name__ == "__main__":
    unittest.main()
