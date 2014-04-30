from datatypes import Strategy
import random


class TitForTatRand(Strategy):
    """
    Tit for tat with Random intervention

    Tit For Tat and Random - Repeat opponent's last choice skewed by a random setting.

    The constructor takes a float between 0 and 1 where
    0 is all tit for tat and 1 is all random
    """

    def __init__(self, skew=0.25):
        self.skew = skew
        self.takes_parameter = True
        # super().__init__()

    def determine_action(self, my_moves, their_moves, turn=0):
        if turn == 0:
            return Strategy.COOPERATE
        else:
            if random.random() > self.skew:
                # skew % of the time
                return their_moves[turn - 1]
            else:
                return random.randrange(2)


if __name__ == "__main__":
    s2 = TitForTatRand()

    print(s2)
    res = []
    n = 10000
    for i in range(n):
        res.append(s2.determine_action([0, 1], [1, 0], 1))

    print(max(res))
    print(min(res))
    print(sum(res)/n)
