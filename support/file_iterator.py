class FileIterator:
    def __init__(self):
        self.__directory_path = ''

    def get_directory_path(self):
        return self.__directory_path

    def set_directory_path(self, dp):
        self.__directory_path = dp

    def get_file(self, path_to_file):
        return open(path_to_file, 'r')
