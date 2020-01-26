from chat import message_builder
from web import json_reader
from chat import chat_room
from utils import web_utils, config
import matplotlib.pyplot as plt

# set global configs
config.set_global_configs()

relative_path_to_messages_jsons = web_utils.get_relative_path_to_messages_jsons()

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

member_tuples = []
tot_messages = 0
for member in messenger_chat.get_chat_members():
    member_name = member.get_member_name()
    num_messages = len(member.get_message_bank())
    total_reacts = member.get_total_reacts()

    # dont include people with no messages or reacts
    if num_messages == 0 or total_reacts == 0:
        continue
    reacts_per_message = total_reacts / num_messages

    # add tuple to list
    member_tuples.append([member_name, num_messages, total_reacts, reacts_per_message])

x = []
y = []
labels = []
for member in member_tuples:
    member_name = member[0].split(" ", 1)[0]
    num_messages = member[1]
    total_reacts = member[2]
    reacts_per_message = member[3]

    print('member: ' + member_name)
    print('num messages: ' + str(num_messages))
    print('num reacts: ' + str(total_reacts))
    print('messages per like ratio: ' + str(reacts_per_message))
    print('------------------------------------------------')

    x.append(num_messages)
    y.append(reacts_per_message)
    labels.append(member_name)
    plt.scatter(num_messages, reacts_per_message)
    plt.text(num_messages+0.01, reacts_per_message+0.01, member_name, fontsize=7)

plt.xlabel('Number of Messages Sent')
plt.ylabel('Likes/Message')
plt.title('2019: Likes/Message VS Number of Messages Sent')

plt.show()

