
from datatypes import Strategy


class Pavlov(Strategy):
    """Pavlov (repeat last choice if good outcome)
    If 5 or 3 points scored in the last round then repeat last choice.
    """

    def determine_action(self, my_moves, their_moves, turn=0):
        if turn == 0:
            return Strategy.COOPERATE
        else:

            if my_moves[turn - 1] == Strategy.COOPERATE:
                if their_moves[turn - 1] == Strategy.COOPERATE:
                    # Both cooperated - keep the ball rolling
                    return my_moves[turn - 1]
                else:
                    # Got taken advantage of
                    # Retribution time
                    return Strategy.DEFECT

            else:
                if their_moves[turn - 1] == Strategy.DEFECT:
                    # we both defected - which is okay
                    return Strategy.DEFECT
                else:
                    # We took advantage - try it again!
                    return Strategy.DEFECT

        return Strategy.COOPERATE
