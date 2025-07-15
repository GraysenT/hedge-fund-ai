def interpret_command(command):
    if 'spawn' in command:
        return 'Spawning agent as requested.'
    return 'Command not recognized.'