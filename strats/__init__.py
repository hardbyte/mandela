from strats.always_cooperate import AlwaysCooperate
from strats.always_defect import AlwaysDefect
from strats.grudger import Grudger
from strats.titfortat import TitForTat
from strats.random_strat import Random
from strats.titfortatrand import TitForTatRand
from strats.titfortatsrand import TitForTatsRand
from strats.remorseful_prober import RemorsefulProber
from strats.naive_prober import NaiveProber
from strats.MLRandomForest import MLRandomForest
from strats.naive_peace_maker import NaivePeaceMaker
from strats.true_peace_maker import TruePeaceMaker
from strats.pavlov import Pavlov, PavlovRandom


all_strategy_classes = [
    AlwaysCooperate,
    AlwaysDefect,
    TitForTat,
    Random,
    TitForTatRand,
    TitForTatsRand,
    RemorsefulProber,
    NaiveProber,
    MLRandomForest,
    NaivePeaceMaker,
    TruePeaceMaker,
    Grudger,
    Pavlov,
    PavlovRandom
]

if __name__ == "__main__":
    s1 = AlwaysCooperate()
    s2 = TitForTat()

    print(s1)
    print(s2)

    print(s2.determine_action([0,1], [1,0], 1))