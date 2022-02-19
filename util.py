import os
import yaml
import sys
import time
from os.path import exists

source_path = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(source_path, "config.yml")
config_template = {
    "commands": [
        {
            "option": {
                "caption": "Create/Append Note",
                "classifications": [
                    "category",
                    "group"
                ],
                "ignore": [
                    "Reports"
                ],
                "max_cols": 4,
                "templates": [
                    {
                        "file": "opportunity.md",
                        "target_paths": [
                            "/FY21",
                            "/FY22",
                            "/FY23",
                        ]
                    },
                    {
                        "file": "technical.md",
                        "target_paths": [
                            "/Technical Notes"
                        ]
                    }
                ]
            }
        }
    ],
    "post_script": None,
    "source_directory": None,
    "working_directory": None
}

def load_config():
    if not config_exists():
        config = config_template
        config['source_directory'] = source_path
        save_config(config_template)
    else:
        with open(config_file, "r") as yml_file:
            config = yaml.load(yml_file, Loader=yaml.FullLoader)
        yml_file.close()
    validate_config(config)
    return config

def config_exists():
    return exists(config_file)

def validate_config(config):
    if config['working_directory'] is None or config['working_directory'] == '':
        if os.getenv('SCRIBE_WD') is not None:
            config['working_directory'] = os.getenv('SCRIBE_WD')
        else:
            entry = None
            caption = "Enter the local path to your notes folder: "
            while not entry:
                entry = input(caption)
                if not os.path.isdir(entry):
                    error_message =  "Path does not exist."
                    reset_entry(caption, error_message)
                    entry = None
            config['working_directory'] = entry
            print("Path saved to config file.\n")
            save_config(config)

def save_config(config):
    with open(config_file, 'w') as file:
        yaml.dump(config, file)

def get_entry(caption, range):
    result = None
    while(result is None):
        entry = input(f"{caption}: ")
        if (entry.isnumeric() and int(entry)-1 in range):
            result = int(entry)-1
        elif (entry.upper() == "X"):
            shutdown(0)
        else:
            reset_entry(caption)
    return result

def reset_entry(caption, error_message):
    if not error_message:
        error_message = "Invalid Entry"
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print(f"{caption}: {error_message}")
    time.sleep(1)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")

def shutdown(iterations):
    if iterations > 0:
        for i in range(iterations+1):
            sys.stdout.write("\r" + "Processing" + "." * i)
            time.sleep(0.2)
            sys.stdout.flush()
        print(" done!")
    print("Goodbye.")
    time.sleep(1)
    quit()

