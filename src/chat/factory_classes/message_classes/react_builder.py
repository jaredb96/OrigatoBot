from . import react


class ReactBuilder:
    def __init__(self):
        FUNNY_CODE = '\u00f0\u009f\u0091\u008d'
        SAD_CODE = '\u00f0\u009f\u0098\u00a2'
        LOVE_CODE = '\u00f0\u009f\u0098\u008d'
        SURPRISED_CODE = '\u00f0\u009f\u0098\u00ae'
        ANGRY_CODE = '\u00f0\u009f\u0098\u00a0'
        UP_CODE = '\u00f0\u009f\u0091\u008d'
        DOWN_CODE = '\u00f0\u009f\u0091\u008e'

        self.reaction_codes = {
            FUNNY_CODE: 'laugh',
            SAD_CODE: 'cry',
            LOVE_CODE: 'heart',
            SURPRISED_CODE: 'shock',
            ANGRY_CODE: 'anger',
            UP_CODE: 'upthumb',
            DOWN_CODE: 'downvote'}

    def build_reacts(self, raw_reacts):
        reacts_output = []
        for r_react in raw_reacts:
            react_object = self.build_react_object_from_raw_react(
                r_react)
            reacts_output.append(react_object)
        return reacts_output

    def build_react_object_from_raw_react(self, raw_react):
        react_output = react.React()
        react_output.actor = raw_react['actor']
        codes = self.reaction_codes
        react_output.reaction_type = codes[raw_react['reaction']]
        return react_output
