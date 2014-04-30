

class Strategy:

    COOPERATE = 1
    DEFECT = 0

    takes_parameter = False

    def __repr__(self):
        p = ""
        if self.takes_parameter:
            p = str(self.skew)
            return "{} ({})".format(self.__class__.__name__, p)
        else:
            return self.__class__.__name__

    def determine_action(self, my_moves, their_moves, turn=0):
        """
        my_moves is a 1xn numpy array
        their_moves is a 1xn numpy array

        Turn is the current turn number

        Returns int: defect = 0, cooperate = 1
        """
        raise NotImplementedError("The base class doesn't do anything!")


def calculate_score(state1, state2):
    """
    Returns the score for strat1 and strat2 as a tuple.
    """

