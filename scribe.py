import util
import note

def get_command():
    print("\rWelcome to Scribe!")
    print("\rSelect an option:")
    commands_len = len(config['commands'])
    for command_index in range(commands_len):
        print(f"\r  {str(command_index+1)}) {str(config['commands'][command_index])}")
    print("\r  X) Exit")
    return util.get_entry("Selection", range(commands_len))

def run_command(command_index):
    if command_index == 0:
        note.run(config)
    else:
        print("Feature not implemented yet... goodbye.")
        quit()
    util.shutdown(3)

if __name__ == "__main__":
    util.load_env_vars()
    config = util.load_config()
    command_index = get_command()
    run_command(command_index)

