from strats.always_cooperate import *
from strats.always_defect import *
from strats.titfortat import *
from strats.random_strat import *


if __name__ == "__main__":
    s1 = AlwaysCooperate()
    s2 = TitForTat()

    print(s1)
    print(s2)

    print(s2.determine_action([0,1], [1,0], 1))