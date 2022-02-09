import os
import yaml
from os import path

authentication_path = '/services/oauth2/token'

def load_config():
    source_path = os.path.dirname(os.path.realpath(__file__))
    working_path = os.path.dirname(source_path)
    config_file = os.path.join(source_path, "config.yml")
    with open(config_file, "r") as ymlfile:
        config = yaml.load(ymlfile, Loader=yaml.FullLoader)
    config['source_path'] = source_path
    config['working_path'] = working_path
    return config

def save_config(config):
    config_file = os.path.join(config['source_path'], "config.yml")
    with open(config_file, 'w') as file:
        yaml.dump(config, file)