from src.chat.factory_classes import message_factory
from src.chat.message_ranking import message_ranker
#from src.web.account_accessors import download_file_account_accessor
from src.web.summary import summary
#from src.web.account_accessors import message_sending_account_accessor
from src.util import file_parser
from setup import load_global_configs
from src.log import *

# Donwload the data source.
#load_global_configs.load_global_configs()
#downloader = download_file_account_accessor.DownloadFileAccountAccessor()
#downloader.download_weekly_message_data()

# Get the data source and process the messages.
parser = file_parser.FileParser()
json_file = open('test_json.json', 'r')
parser.json_file = json_file
raw_messages = parser.get_raw_messages_from_chat()
names_to_member = parser.get_names_to_member_map()
title = parser.get_chat_title()
thread_path = parser.get_chat_thread_path()
m_factory = message_factory.MessageFactory()
messages = m_factory.build_messages(raw_messages)
ranker = message_ranker.MessageRanker()
top_three_messages = ranker.get_top_three_messages(messages)
summary_message = summary.Summary(top_three_messages)
print(summary_message.top_three_messages)

# Send the summary message to the chat.
#message_sender = message_sending_account_accessor.\
#    MessageSendingAccountAccessor()
#message_sender.send_message_to_chat(summary_message)