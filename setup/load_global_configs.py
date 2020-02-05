# global dictionary used to store information relative to user
CONFIGS = {}


def load_global_configs():
    file = open('setup/setup.txt')
    for line in file:
        key, value = line.strip().split('=')
        CONFIGS[key.strip()] = value.strip()
