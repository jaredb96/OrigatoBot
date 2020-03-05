import os


class LogWriter:
    def __init__(self):
        self.__log_file_path = os.getcwd() + '/logs.txt'

    def log_info_from_map(self, info: dict):
        self.write_perforated_line()

        for key in info.keys():
            self.log(key, info[key])

        self.write_perforated_line()

    def write_perforated_line(self):
        with open(self.__log_file_path, 'a+') as log_file:
            log_file.write('--------------------\n')

    def log(self, tag: str, content: str):
        with open(self.__log_file_path, 'a+') as log_file:
            content = tag.upper() + ": " + str(content)
            log_file.write(content + '\n')