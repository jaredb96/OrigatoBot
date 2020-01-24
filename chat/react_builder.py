from chat import react


class ReactBuilder:
    def __init__(self):
        self.__reaction_data_map = {}
        self.__reaction_code_map = {'\u00f0\u009f\u0091\u008d': 'laugh'}

    def get_reaction_data_map(self):
        return self.__reaction_data_map

    def set_reaction_data_map(self, rdm):
        self.__reaction_data_map = rdm

    def create_react_object(self):
        '''
        Create a react object from the stored data map
        :return: react object with data from map
        '''
        react_obj = react.React()
        reaction_data_map = self.get_reaction_data_map()
        if not reaction_data_map:
            return react_obj
        react_obj.set_reaction_type(
            self.__reaction_code_map[reaction_data_map['reaction']])
        react_obj.set_actor(reaction_data_map['actor'])
        return react_obj
