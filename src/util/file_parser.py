from . import directory_walker
import json


class FileParser:
    def __init__(self):
        self.json_file_path = None

    def get_raw_messages_from_file(self):
        json_file = open(self.json_file_path)

        json_as_string = json_file.read()
        json_as_string = self.clean_json_string(json_as_string)

        json_object = json.loads(json_as_string)

        return json_object['messages']

    def get_names_to_member_map(self):
        json_file = open(self.json_file_path)
        json_object = json.load(json_file)
        return json_object['participants']

    def get_chat_title(self):
        json_file = open(self.json_file_path)
        json_object = json.load(json_file)
        return json_object['title']

    def get_chat_thread_path(self):
        json_file = open(self.json_file_path)
        json_object = json.load(json_file)
        return json_object['thread_path']

    def clean_json_string(self, json_as_string):
        json_as_string = json_as_string.replace("\\u00e2\\u0080\\u0099", "\'")
        json_as_string = json_as_string.replace("\\u00e2\\u0080\\u009c", "\'")
        json_as_string = json_as_string.replace("\\u00e2\\u0080\\u009d", "\'")

        return json_as_string
