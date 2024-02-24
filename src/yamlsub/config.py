from dotenv import load_dotenv
from pyaml_env import parse_config

class Config:
    def __init__(self, yaml_path='config.yaml', env_path='.env'):
        load_dotenv(env_path, verbose=True)
        self.__config = parse_config(yaml_path)

    def get_config(self):
        return self.__config
    
    def get_config_key(self, key):
        return self.__config[key]
