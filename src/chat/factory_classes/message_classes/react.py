class React:
    def __init__(self, reaction_type='', actor=''):
        self.reaction_type = reaction_type
        self.actor = actor

    def __eq__(self, other):
        return self.__reaction_type == other.get_reaction_type() and \
               self.__actor == other.get_actor()
