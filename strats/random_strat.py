from datatypes import Strategy
import random


class Random(Strategy):

    def determine_action(self, my_moves, their_moves, turn=0):
        return random.randrange(2)


if __name__ == "__main__":

    s = Random()

    print(s.determine_action([0, 1], [0, 1], 1))

