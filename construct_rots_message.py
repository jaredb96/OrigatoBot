from chat import chat_room
from numpy.polynomial.polynomial import polyfit

def get_rots_message(messenger_chat: chat_room):
    num_messages_per_user = []
    num_reacts_received_per_user = []
    name_to_chat_member_mapping = {}
    for member in messenger_chat.get_chat_members():
        member_name = member.get_member_name()
        name_to_chat_member_mapping[member_name] = member

        num_messages = len(member.get_message_bank())
        total_reacts = member.get_total_reacts()

        # dont include people with no messages
        if num_messages < 50:
            continue

        num_messages_per_user.append(num_messages)
        num_reacts_received_per_user.append(total_reacts)

    b, m = polyfit(num_messages_per_user, num_reacts_received_per_user, 1)

    author_to_origato_score_mapping = {}
    for member in messenger_chat.get_chat_members():
        member_name = member.get_member_name()
        num_messages = len(member.get_message_bank())
        total_reacts = member.get_total_reacts()

        expected = b + m * num_messages
        actual = total_reacts

        origato_score = ((actual - expected) / expected) * 100
        author_to_origato_score_mapping[member_name] = origato_score

    sorted_mappings = sorted(author_to_origato_score_mapping.items(), key=lambda x: x[1], reverse=True)
    top_scores = sorted_mappings[0:3]

    rankings_message = ""
    rankings_message += 'In addition, here are the top 3 origato-scorers of the week!\n'

    for i, mapping in enumerate(top_scores):
        author_name = mapping[0]
        first_name = author_name.split(' ')[0]
        score = mapping[1]

        member = name_to_chat_member_mapping[author_name]
        total_reacts = member.get_total_reacts()
        total_messages = len(member.get_message_bank())

        rankings_message += str(i + 1) + ') *' + first_name + '*: \n'

        rankings_message += 'With a total of ' + str(total_reacts) + ' reacts and ' \
                            + str(total_messages) + ' messages sent, \n'

        rankings_message += author_name + ' received a score of *' + str(round(score, 2)) + '%* '
        if score >= 0:
            rankings_message += 'above the average!'
        else:
            rankings_message += 'below the average!'

        rankings_message += '\n-------------------------------------------------\n'

    return rankings_message



