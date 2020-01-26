from utils.web_utils import *
from web.json_download_logger import *
from chat import chat_room, message_builder
from web import json_reader, json_download_logger
from utils import web_utils, config
import matplotlib.pyplot as plt


def get_converted_timestamps(timestamp_ms):
    num_years = int(timestamp_ms / 1000 / 60 / 60 / 24 / 365)
    timestamp_ms -= num_years * 365 * 24 * 60 * 60 * 1000

    num_days = int(timestamp_ms / 1000 / 60 / 60 / 24)
    timestamp_ms -= num_days * 24 * 60 * 60 * 1000

    num_hours = int(timestamp_ms / 1000 / 60 / 60)
    timestamp_ms -= num_hours * 60 * 60 * 1000

    num_minutes = int(timestamp_ms / 1000 / 60)
    timestamp_ms -= num_minutes * 60 * 1000

    # get rid of 5 hour offset
    num_hours -= 5

    # case where becomes negative (yesterday)
    if num_hours < 0:
        num_hours += 24

    converted_time = num_hours + num_minutes/60
    return converted_time


def get_messages_histogram_for_range(start_date, end_date):
    # download message data
    json_downloader_bot = json_download_logger.JsonDownloadLogger()
    json_downloader_bot.download_message_data(start_date, end_date)

    # unzip data and get path to it
    web_utils.unzip_message_data()
    json_files_directory = web_utils.get_relative_path_to_messages_jsons()

    # create json parser
    m_factory = message_builder.MessageBuilder()
    j_parser = json_reader.JsonReader(json_files_directory=json_files_directory)
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

    chat_messages = sorted(chat_messages, key=lambda x: x.get_message_id(), reverse=False)

    converted_times = []
    for message in chat_messages:
        timestamp = message.get_message_id()
        converted_times.append(get_converted_timestamps(timestamp))

    range = str(start_date.month) + '-' + str(start_date.day) + '_' + str(end_date.month) + '-' + str(end_date.day)
    plt.hist(converted_times, bins=100)
    plt.xlabel('Time (military time)')
    plt.ylabel('Messages Sent (count)')
    plt.title('Origato Chat \'Lit Times\' ' + range + 'ish ya yeet')
    plt.savefig('figures/Lit_Times_' + range + '.png')
    plt.clf()

    web_utils.downloads_cleanup()


# set global configs
config.set_global_configs()

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(7)

get_messages_histogram_for_range(start_date=start_date, end_date=end_date)


