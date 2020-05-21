# set HEADLESS to True if you don't want a browser to open up
# set HEADLESS to False if you want a browser to open up
HEADLESS = True

# global dictionary used to store information relative to user
CONFIGS = {}


def load_global_configs():
    file = open('setup/config.txt')
    for line in file:
        key, value = line.strip().split('=')
        CONFIGS[key.strip()] = value.strip()
