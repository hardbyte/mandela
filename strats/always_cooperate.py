from datatypes import Strategy


class AlwaysCooperate(Strategy):

    def determine_action(self, my_moves, their_moves, turn=0):
        return 1


