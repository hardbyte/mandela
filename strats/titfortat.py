from datatypes import Strategy


class TitForTat(Strategy):
    """
    Tit for tat

    Repeat opponent's last choice
    """
    def determine_action(self, my_moves, their_moves, turn=0):
        if turn == 0:
            return Strategy.COOPERATE
        else:
            last_move = their_moves[turn - 1]
            return last_move


if __name__ == "__main__":
    s2 = TitForTat()

    print(s2)
    print(s2.determine_action([0,1], [1,0], 1))