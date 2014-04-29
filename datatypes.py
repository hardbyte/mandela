

class Strategy:

    def determine_action(self, history, turn=0):
        """
        History is a 2 X n numpy array
        Turn is the index

        Returns int: defect = 0, cooperate = 1
        """
        raise NotImplementedError("The base class doesn't do anything!")


def calculate_score(state1, state2):
    """
    Returns the score for strat1 and strat2 as a tuple.
    """

