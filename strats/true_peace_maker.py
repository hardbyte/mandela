# Naive Peace Maker


from datatypes import Strategy
import random


class TruePeaceMaker(Strategy):
    """
    True Peace Maker
    (hybrid of Tit For Tat and Tit For Two Tats with Random Co-operation)

    Co-operate unless opponent defects twice in a row, then
    defect once, but sometimes make peace by co-operating in lieu of defecting.
    """
    takes_parameter = True

    def __init__(self, skew=0.25):
        self.skew = skew


    def determine_action(self, my_moves, their_moves, turn=0):
        if turn == 0:
            return Strategy.COOPERATE
        else:
            move = Strategy.COOPERATE
            if all(m == Strategy.DEFECT for m in [their_moves[turn - 2], their_moves[turn - 1]]):
                # tit for tat comes into play if they have defected twice
                if random.random() > self.skew:
                    # Make peace
                    return Strategy.COOPERATE
                else:
                    # Punish them!
                    return Strategy.DEFECT
            return move


