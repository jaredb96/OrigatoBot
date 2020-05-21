from . import general_message_factory
from . message_classes import deleted_message


class DeletedMessageMessageFactory(general_message_factory.GeneralMessageFactory):
    def build_message(self, raw_message):
        deleted_message_output = deleted_message.DeletedMessage()
        deleted_message_output.author = raw_message['sender_name']
        deleted_message_output.message_id = raw_message['timestamp_ms']
        return deleted_message_output




