import platform
import os
from setup.load_global_configs import CONFIGS
import zipfile
import shutil
from bs4 import BeautifulSoup


class DirectoryWalker:
    def get_origato_messages_directory_name(self):
        # windows media/messages directory are the same
        if platform.system() == 'Windows':
            return self.get_origato_directory_name_windows()

        # linux (and Mac?) downloads store messages in
        # directory with lowercase chat name
        elif platform.system() == 'Linux' or platform.system() == \
                'Darwin':
            for directory_name in os.listdir('messages/inbox'):
                if 'origato' in directory_name and 'origatoresurrected' not in directory_name:
                    return directory_name

        # default, should never reach
        return ''

    def get_origato_media_directory_name(self):
        # windows media/messages directory are the same
        if platform.system() == 'Windows':
            return self.get_origato_directory_name_windows()

        # linux (and Mac?) downloads store media in directory with
        # uppercase chat name
        elif platform.system() == 'Linux' or platform.system() == \
                'Darwin':
            for directory_name in os.listdir('messages/inbox'):
                if 'ORIGATO' in directory_name and 'ORIGATORESURRECTED' not in directory_name:
                    return directory_name

        # default, should never reach
        return ''

    def get_origato_directory_name_windows(self):
        origato_chat_name = ""
        for directory_name in os.listdir('messages/inbox'):
            if 'ORIGATO' in directory_name.upper() and 'ORIGATORESURRECTED' not in directory_name.upper():
                origato_chat_name = directory_name
        return origato_chat_name

    def unzip_message_data(self):
        print('unzipping downloaded files...')
        downloads_directory = CONFIGS['downloads_directory']
        zipfile_name = CONFIGS['zipfile_name']
        path_to_zip_file = downloads_directory + zipfile_name

        destination_directory = os.getcwd()
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(destination_directory)

        origato_media_directory_name = self.\
            get_origato_media_directory_name()
        self.__convert_all_mp4_files_to_mp3(
            destination_directory + '/messages/inbox/' +
            origato_media_directory_name + '/audio'
        )

    def get_relative_path_to_messages_jsons(self):
        origato_messages_directory_name = self.\
            get_origato_messages_directory_name()

        relative_path_to_messages_json = \
            'messages/inbox/' + origato_messages_directory_name + '/'
        return relative_path_to_messages_json

    def __convert_all_mp4_files_to_mp3(self, path):
        if not os.path.exists(path):
            return
        print('converting audio files from mp4 to mp3...')
        for filename in os.listdir(path):
            base_file, ext = os.path.splitext(filename)
            if ext == ".mp4":
                os.rename(path + '/' + filename,
                          path + '/' + base_file + ".mp3")

    def downloads_cleanup(self):
        download_dir = CONFIGS['downloads_directory']
        zipfile_name = CONFIGS['zipfile_name']
        path_to_zip_file = download_dir + zipfile_name

        if os.path.exists(path_to_zip_file):
            os.remove(path_to_zip_file)

        path_to_messages_folder = os.getcwd() + '/messages'
        if os.path.exists(path_to_messages_folder):
            shutil.rmtree(path_to_messages_folder)

    # useful function for debugging, prints html of an element
    # grabbed by selenium/other web scrapers
    def pretty_print_html_element(self, block):
        html_string = block.get_attribute('outerHTML')
        print(BeautifulSoup(html_string, 'html.parser').prettify())
