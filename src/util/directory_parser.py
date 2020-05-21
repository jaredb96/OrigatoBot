from . import directory_walker
import json
import os
from . import file_parser


class DirectoryParser:
    def __init__(self):
        self.jsons_directory = None

    def get_raw_messages_from_chat(self):
        raw_messages = []

        json_parser = file_parser.FileParser()
        num_of_json_files = self.get_number_of_json_files()
        for i in range(1, num_of_json_files+1):
            json_parser.json_file_path = self.jsons_directory + 'message_' + str(i) + '.json'
            raw_messages.extend(json_parser.get_raw_messages_from_file())

        return raw_messages

    def get_names_to_member_map(self):
        parser = file_parser.FileParser()
        parser.json_file_path = self.jsons_directory + 'message_1.json'
        return parser.get_names_to_member_map()

    def get_chat_title(self):
        parser = file_parser.FileParser()
        parser.json_file_path = self.jsons_directory + 'message_1.json'
        return parser.get_chat_title()

    def get_chat_thread_path(self):
        parser = file_parser.FileParser()
        parser.json_file_path = self.jsons_directory + 'message_1.json'
        return parser.get_chat_thread_path()

    def get_number_of_json_files(self):
        # find how how many message jsons there are (depends on how many messages there are to process)
        num_json_files = 0
        for directory_name in os.listdir(self.jsons_directory):
            if 'message_' in directory_name and '.json' in directory_name:
                num_json_files += 1

        return num_json_files
