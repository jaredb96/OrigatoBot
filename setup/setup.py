import os
import subprocess
import platform


def setup():
    print('--------- INSTALLING PROJECT DEPENDENCIES ---------')
    install_dependencies()

    print('--------- GENERATING CONFIG FILE ---------')
    generate_config_file()


def install_dependencies():
    dependencies = generate_dependencies_list()

    for package in dependencies:
        print('installing ' + package)
        install_python_package(package)


def install_python_package(package):
    # Windows does not recognize 'python3' as command
    operating_system = platform.system()
    if operating_system == 'Windows':
        installation_command = 'python -m pip install ' + package
    else:
        installation_command = 'python3 -m pip install ' + package

    print('RUNNING: ' + installation_command + '...')
    os.system(installation_command)



def generate_dependencies_list():
    file = open('requirements.txt')
    dependencies = []
    for line in file:
        package = line[0:line.find('=')]
        dependencies.append(package)
    return dependencies


def generate_config_file():
    username = input('Please enter the username of the bot account: ')
    password = input('Please enter the password of the bot account: ')
    downloads_directory = input('Please enter the directory where the bot will download the zipfile into\n'
                                '(both forward and back slashes acceptable, and and make sure to end with a slash): ')
    zipfile_name = input('Please enter the name of the zipfile that would be downloaded from fb settings\n'
                         '(include \'.zip\' extension): ')

    greeting_message = input('Enter the message you want the bot to greet the chat with!: ')
    farewell_message = input('Enter the message you want the bot to leave the chat with!: ')

    config_file_name = 'config.txt'
    config_file = open('setup/' + config_file_name, 'w+')

    config_file.write('username = ' + username + '\n')
    config_file.write('password = ' + password + '\n')
    config_file.write('downloads_directory = ' + downloads_directory + '\n')
    config_file.write('zipfile_name = ' + zipfile_name + '\n')
    config_file.write('greeting_message = ' + greeting_message + '\n')
    config_file.write('farewell_message = ' + farewell_message + '\n')

    config_file.close()

    print(config_file_name + ' generated successfully!\n'
          'remember you can always go into the setup folder and change the file by hand.')


"""
uncomment this function and run when ready to install dependencies and run configurations
This function installs all dependencies needed for the project, and generates text file for user configurations

make sure to run this file from the root directory of the repo (Your directory should be /path/to/WebScrapeChatBot/)
"""
setup()
