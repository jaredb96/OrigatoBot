from chat import message_builder
from web import json_reader, message_with_media_send_logger
from chat import chat_room
from web import json_download_logger
from config import config
import time
from construct_rots_message import *

# set global configs
config.set_global_configs()

# download message data
json_downloader_bot = json_download_logger.JsonDownloadLogger()
json_downloader_bot.download_weekly_message_data()

# unzip data and get path to it
json_downloader_bot.unzip_message_data()
relative_path_to_messages_jsons = json_downloader_bot.get_relative_path_to_messages_jsons()

# create json parser
m_factory = message_builder.MessageBuilder()
j_parser = json_reader.JsonReader(json_files_directory=relative_path_to_messages_jsons)
m_factory.set_json_reader(j_parser)

# get chat members
chat_member_names = j_parser.make_chat_member_names_list()
messenger_chat = chat_room.ChatRoom()
chat_members = messenger_chat.make_chat_members_from_names_list(
    chat_member_names)
messenger_chat.set_chat_members(chat_members)

# get chat messages and assign to chat members
chat_messages = m_factory.make_list_of_messages()
messenger_chat.assign_messages_to_members(chat_messages)

rots_ranking_message = get_rots_message(messenger_chat)
top_three_messages = messenger_chat.get_top_k_messages_with_ties(3)

# send summary to origato chat
m_sender = message_with_media_send_logger.MessageWithMediaSendLogger(top_three_messages,
                                                                     rots_ranking_message=rots_ranking_message)
m_sender.send_summary()

# sleep to see the result before window closes
time.sleep(3)

print('summary message sent, deleting downloaded files...')

# delete zip file and unzipped directory
json_downloader_bot.downloads_cleanup()

print('cleanup complete! everythings finished :)')
