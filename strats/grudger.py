# Naive Peace Maker


from datatypes import Strategy
import random


class Grudger(Strategy):
    """
    Grudger (Co-operate, but only be a sucker once)
    Co-operate until the opponent defects. Then always defect unforgivingly.
    """
    def __init__(self):
        self.has_defected = False

    def determine_action(self, my_moves, their_moves, turn=0):
        if turn > 0 and their_moves[turn-1] == Strategy.DEFECT:
            self.has_defected = True

        if turn == 0 or not self.has_defected:
            return Strategy.COOPERATE
        else:
            return Strategy.DEFECT


