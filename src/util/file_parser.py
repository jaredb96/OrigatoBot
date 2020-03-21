from . import directory_walker
import json


class FileParser:
    def __init__(self):
     #   walker.unzip_message_data()
      #  relative_path_to_json
    #
     #'message_1.json'
        self.json_file = None

    def get_raw_messages_from_chat(self):
        json_object = json.load(self.json_file)
        return json_object['messages']

    def get_names_to_member_map(self):
        json_object = json.loads(self.json_file)
        return json_object['participants']

    def get_chat_title(self):
        json_object = json.load(self.json_file)
        return json_object['title']

    def get_chat_thread_path(self):
        json_object = json.load(self.json_file)
        return json_object['thread_path']