import yaml
import os

__config = None


def config_yaml():
    file_directory = os.path.dirname(__file__)
    file = os.path.join(file_directory, 'config.yaml')

    global __config
    if not __config:
        with open(file, mode='r') as f:
            __config = yaml.safe_load(f)
    return __config


