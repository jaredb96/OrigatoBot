class React:
    def __init__(self, reaction_type='', actor=''):
        self.__reaction_type = reaction_type
        self.__actor = actor

    def get_reaction_type(self):
        return self.__reaction_type

    def set_reaction_type(self, rt):
        self.__reaction_type = rt

    def get_actor(self):
        return self.__actor

    def set_actor(self, ac):
        self.__actor = ac

    def __eq__(self, other):
        return self.__reaction_type == other.get_reaction_type() and \
               self.__actor == other.get_actor()
