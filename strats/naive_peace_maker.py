# Naive Peace Maker


from datatypes import Strategy
import random


class NaivePeaceMaker(Strategy):
    """
    (Tit For Tat with Random Co-operation)
    Repeat opponent's last choice (ie Tit For Tat), but
    sometimes make peace by co-operating in lieu of defecting.
    """
    takes_parameter = True

    def __init__(self, skew=0.25):
        self.skew = skew


    def determine_action(self, my_moves, their_moves, turn=0):
        if turn == 0:
            return Strategy.COOPERATE
        else:

            # tit for tat
            # Reciprocate their last move
            move = their_moves[turn - 1]
            if move == Strategy.DEFECT and random.random() > self.skew:
                # Make peace
                return Strategy.COOPERATE
            return move


