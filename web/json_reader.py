"""
json_reader.py - ChatRoom web scraping class for OrigatoBot.
@author: Jared Barrow
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import os

class JsonReader:
    def __init__(
            self,
            json_files_directory=None,
            member_names=[],
            name_to_messages={}):
        self.__json_files_directory = json_files_directory
        self.__member_names = member_names
        self.__name_to_message_data_map = name_to_messages

    def get_json_files_directory(self):
        return self.__json_files_directory

    def set_json_files_directory(self, json_files_directory):
        self.__json_files_directory = json_files_directory

    def get_member_names(self):
        return self.__member_names

    def set_member_names(self, mn):
        self.__member_names = mn

    def get_name_to_message_data_map(self):
        return self.__name_to_message_data_map

    def set_name_to_message_data_map(self, ntm):
        self.__name_to_message_data_map = ntm

    def make_chat_member_names_list(self):
        names_list = []
        json_file = open(self.get_json_files_directory() + 'message_1.json')
        json_data = json.load(json_file)
        names_map_list = json_data['participants']
        for name_map in names_map_list:
            names_list.append(name_map['name'])
        return names_list

    def make_json_data_map(self):
        """
        Create a mapping for data for each ChatMember.
        :return: a mapping from message author name to
        [(message1_id, message1_text, number_of_reacts),
        (message2_id, message2_text, number_of_reacts)]
        """
        json_data_map = {}

        json_files_directory = self.get_json_files_directory()

        # find how how many message jsons there are (depends on how many messages there are to process)
        num_json_files = 0
        for directory_name in os.listdir(json_files_directory):
            if 'message_' in directory_name and '.json' in directory_name:
                num_json_files += 1

        # iterate thru all json files, adding all messages to map
        for i in range(1, num_json_files+1):

            curr_json_file_path = self.get_json_files_directory() + 'message_' + str(i) + '.json'
            self.add_messages_from_json_file_to_data_map(json_data_map, curr_json_file_path)

        return json_data_map

    def add_messages_from_json_file_to_data_map(self, json_data_map, curr_json_file_path):
        json_file = open(curr_json_file_path)

        # apostrophes and quotations are encoded weird in this shit
        json_string = json_file.read()
        json_string = json_string.replace("\\u00e2\\u0080\\u0099", "\'")
        json_string = json_string.replace("\\u00e2\\u0080\\u009c", "\'")
        json_string = json_string.replace("\\u00e2\\u0080\\u009d", "\'")

        json_data = json.loads(json_string)

        # add users to the data map (if not already added)
        names_list = json_data['participants']
        for member_name in names_list:
            name = member_name['name']
            if name not in json_data_map.keys():
                json_data_map[name] = []

        messages = json_data['messages']

        for message in messages:
            author_name = message['sender_name']
            # skip deactivated users
            if author_name == 'Facebook User':
                continue

            message_id = message['timestamp_ms']

            # read in messages that are either text-based, photo-based, or audio-based
            if 'content' in message.keys():
                message_text = message['content']
                message_media_uri = ''
            elif 'photos' in message.keys() or 'audio_files' in message.keys() or 'gifs' in message.keys():
                message_text = ''
                if 'photos' in message.keys():
                    media_key = 'photos'
                elif 'audio_files' in message.keys():
                    media_key = 'audio_files'
                else:
                    media_key = 'gifs'

                # if photo/audio/gif based, only use first photo/gif/audio clip
                first_media = message[media_key][0]
                message_media_uri = first_media['uri']
            else:
                continue

            # see if message has any reactions
            try:
                number_of_reacts = len(message['reactions'])
            except KeyError:
                number_of_reacts = 0

            # add message info to data map
            json_data_map[author_name].append(
                (message_id, message_text, number_of_reacts, message_media_uri))

        json_file.close()
