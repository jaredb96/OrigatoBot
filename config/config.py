# global dictionary used to store information relative to user
CONFIGS = {}


def set_global_configs():
    file = open('config.txt')
    for line in file:
        key, value = line.strip().split('=')
        CONFIGS[key.strip()] = value.strip()
