def compile_time_script(memory):
    return {
        "init_state": memory[0],
        "core_loop": memory[1:-1],
        "exit_condition": memory[-1]
    }