import util
import note

def get_command():
    print("\rWelcome to Scribe!")
    print("\rSelect an option:")
    commands_len = len(config['commands'])
    for option_index in range(commands_len):
        print(f"\r  {str(option_index+1)}) {str(config['commands'][option_index]['option']['caption'])}")
    print("\r  X) Exit")
    return util.get_entry("Selection", range(commands_len))

def run_command(option_index):
    if option_index == 0:
        note.run(config, config['commands'][option_index]['option'])
    else:
        print("Feature not implemented yet... goodbye.")
        quit()
    util.shutdown(3)

if __name__ == "__main__":
    initial_run = not util.config_exists()
    config = util.load_config()
    if initial_run:
        note.create_scratchpad(config)
    option_index = get_command()
    run_command(option_index)

