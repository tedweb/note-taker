import util
import note
import os
import re

def get_command():
    print("\rWelcome to Scribe!")
    print("\rSelect an option:")
    commands_len = len(config['commands'])
    for option_index in range(commands_len):
        print(f"\r  {str(option_index+1)}) {str(config['commands'][option_index]['option']['caption'])}")
    print("\r  X) Exit")
    return util.get_entry("Selection", range(commands_len))

def run_command(option_index):
    result = None
    if option_index == 0:
        result = note.run(config, config['commands'][option_index]['option'])
    else:
        print("Feature not implemented yet... goodbye.")
        quit()
    return result

def run_post_command(target_file):
    if target_file and config['post_script'] and config['post_script']:
        message = "Open file? [Y]"
        entry = input(f"{message}: ")
        if entry == '':
            entry = 'Y'
        if entry.upper()[0:1] == 'Y':
            var_regex = r"\{(.*?)\}"
            launch_command = config['post_script']
            launch_command = re.sub(var_regex, target_file, launch_command)
            os.system(launch_command)

if __name__ == "__main__":
    initial_run = not util.config_exists()
    config = util.load_config()
    if initial_run:
        note.create_scratchpad(config)
    option_index = get_command()
    target_file = run_command(option_index)
    run_post_command(target_file)
    util.shutdown(3)


