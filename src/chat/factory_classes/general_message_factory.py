from . message_classes import react_builder


class GeneralMessageFactory:
    def __init__(self):
        self.react_builder = react_builder.ReactBuilder()
        pass

    def build_message(self):
        """
        Build message method, to be overriden by subclasses.
        """
        pass

    def build_reactions(self, raw_reactions):
        r_builder = self.react_builder
        reactions = r_builder.build_reacts(raw_reactions)
        return reactions


