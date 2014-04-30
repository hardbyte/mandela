
from datatypes import Strategy
import random


class NaiveProber(Strategy):
    """Naive Prober
    (Tit For Tat with Random Defection)

    - Repeat opponent's last choice (ie Tit For Tat), but sometimes
     probe by defecting in lieu of co-operating
    """
    takes_parameter = True

    def __init__(self, skew=0.25):
        self.skew = skew

    def determine_action(self, my_moves, their_moves, turn=0):
        if turn == 0:
            return Strategy.COOPERATE
        else:
            # skew % of the time
            if random.random() > self.skew:
                # tit for tat mode
                # Reciprocate their move
                return their_moves[turn - 1]
            else:
                return Strategy.DEFECT


