from src.chat.factory_classes import message_factory
from src.chat.message_ranking import message_ranker
from src.web.account_accessors import download_file_account_accessor
from src.web.summary import summary
from src.web.account_accessors import message_sending_account_accessor
from src.util import directory_walker,directory_parser
from setup import load_global_configs

# Download the data source.
load_global_configs.load_global_configs()
downloader = download_file_account_accessor.DownloadFileAccountAccessor()
# downloader.download_weekly_message_data()
downloader.download_this_years_message_data()

walker = directory_walker.DirectoryWalker()
walker.unzip_message_data()
path_to_json_directory = walker.get_relative_path_to_messages_jsons()
print(path_to_json_directory)

# Get the data source and process the messages.
parser = directory_parser.DirectoryParser()
parser.jsons_directory = path_to_json_directory

raw_messages = parser.get_raw_messages_from_chat()
names_to_member = parser.get_names_to_member_map()
title = parser.get_chat_title()
thread_path = parser.get_chat_thread_path()
m_factory = message_factory.MessageFactory()
messages = m_factory.build_messages(raw_messages)
ranker = message_ranker.MessageRanker()
top_three_messages = ranker.get_top_three_messages(messages)
summary_message = summary.Summary(top_three_messages)

# for message in top_three_messages:
#     print('author: ' + message.author)
#     try:
#         print('content: ' + message.text)
#     except:
#         print('uri: ' + message.media_uri)
#     print('num reacts: ' + str(message.get_number_of_reacts()))

# Send the summary message to the chat.
message_sender = message_sending_account_accessor.\
   MessageSendingAccountAccessor()
message_sender.send_summary_to_chat(summary_message)

walker.downloads_cleanup()