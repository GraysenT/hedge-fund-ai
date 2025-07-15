def recombine_dna(config_a, config_b):
    new_config = {}
    for k in config_a:
        if isinstance(config_a[k], (int, float)):
            new_config[k] = (config_a[k] + config_b.get(k, config_a[k])) / 2
        else:
            new_config[k] = config_a[k]
    return new_config