import datetime
from ya_yeet_logging_stoof_for_jawed import log_writer


class Logger:
    def __init__(self, chat_room, top_messages):
        self.__logwriter = log_writer.LogWriter()
        self.__chat_room = chat_room
        self.__top_messages = top_messages

    def gen_map_for_chat_data(self):

        current_timestamp = datetime.datetime.now()
        todays_day = current_timestamp.day
        todays_month = current_timestamp.month
        todays_year = current_timestamp.year
        todays_date = str(todays_month) + ', ' + str(todays_day) + ' ' + str(todays_year)

        messages_processed = len(self.__chat_room.get_all_messages())
        members_in_chat = len(self.__chat_room.get_chat_members())
        num_top_messages = len(self.__top_messages)

        chat_data_mapping = {
            'date executed': todays_date,
            'messages processed': messages_processed,
            'members in chat': members_in_chat,
            'number of top messages sent': num_top_messages
        }

        return chat_data_mapping

    def log_execution_summary(self):
        map = self.gen_map_for_chat_data()
        self.__logwriter.log_info_from_map(info=map)
