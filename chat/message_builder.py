from chat import message
from web import json_reader


class MessageBuilder:
    """
    Creates message objects.
    @author: Jared Barrow
    """
    def __init__(self, j_reader=None):
        self.__json_reader = j_reader

    def get_json_reader(self):
        return self.__json_reader

    def set_json_reader(self, jr):
        self.__json_reader = jr

    def make_list_of_messages(self):
        messages_list = []
        parser = self.get_json_reader()
        json_data_map_for_messages = parser.make_json_data_map()

        for member in json_data_map_for_messages:
            message_data_list = json_data_map_for_messages[member]
            for message_data in message_data_list:
                new_message = message.Message()
                new_message.set_author(member)
                new_message.set_message_id(message_data[0])
                new_message.set_text(message_data[1])
                new_message.set_number_of_reacts(message_data[2])
                new_message.set_media_uri(message_data[3])
                messages_list.append(new_message)

        return messages_list



