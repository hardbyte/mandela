from datatypes import Strategy


class AlwaysCooperate(Strategy):

    def determine_action(self, history, turn=0):
        return 1


