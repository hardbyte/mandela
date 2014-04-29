
from datatypes import Strategy


class AlwaysDefect(Strategy):

    def determine_action(self, history, turn=0):
        return 0


if __name__ == "__main__":
    print("testing Always Defect strat")