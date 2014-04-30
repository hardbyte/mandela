from datatypes import Strategy
import random


class TitForTatsRand(Strategy):
    """
    Tit for tats with Random intervention

    Tit For Two Tats and Random
    Like Tit For Tat except that opponent must make the same choice twice in a row before it is reciprocated.
    Choice is skewed by random setting.

    The constructor takes a float between 0 and 1 where
    0 is all tit for tat and 1 is all random
    """

    def __init__(self, skew=0.25):
        self.skew = skew
        self.takes_parameter = True
        # super().__init__()

    def determine_action(self, my_moves, their_moves, turn=0):
        if turn < 2:
            return Strategy.COOPERATE
        else:
            # skew % of the time
            if random.random() > self.skew:
                # tit for tat mode
                if their_moves[turn - 1] == their_moves[turn - 2]:
                    # Reciprocate their move
                    return their_moves[turn - 2]
                else:
                    return Strategy.COOPERATE

            # else we are purely random
            return random.randrange(2)


if __name__ == "__main__":
    s2 = TitForTatsRand()

    print(s2)
    res = []
    n = 10000
    for i in range(n):
        res.append(s2.determine_action([0, 1], [1, 0], 1))

    print(max(res))
    print(min(res))
    print(sum(res)/n)
