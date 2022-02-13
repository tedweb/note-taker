import os
import yaml
import sys
import time
from os import path
from dotenv import load_dotenv

authentication_path = '/services/oauth2/token'

def load_env_vars():
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, '.env'))

def load_config():
    source_path = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(source_path, "config.yml")
    with open(config_file, "r") as ymlfile:
        config = yaml.load(ymlfile, Loader=yaml.FullLoader)

    if config['working_directory'] == None:
        if os.getenv('SCRIBE_WD') is not None:
            config['working_directory'] = os.getenv('SCRIBE_WD')
        else:
            config['working_directory'] = source_path
    config['source_directory'] = source_path
    return config

def save_config(config):
    config_file = os.path.join(config['source_path'], "config.yml")
    with open(config_file, 'w') as file:
        yaml.dump(config, file)

def get_entry(caption, range):
    result = None

    while(result is None):
        entry = input(f"{caption}: ")
        if (entry.isnumeric() and int(entry) in range):
            result = int(entry)
        elif (entry.upper() == "X"):
            print("Goodbye.")
            quit()
        else:
            reset_entry(caption)
    return result

def reset_entry(caption):
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print(f"{caption}: Invalid Entry")
    time.sleep(1)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


