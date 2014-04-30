import strats
import numpy as np
import matplotlib.pyplot as pl

number_of_rounds = 10

# Strategy.COOPERATE
# Strategy.DEFECT

def pairs(s):
    for i in range(0, len(s)-1):
        for j in range(i+1, len(s)):
            yield (s[i], s[j])

game_array = np.array([[5,3],[3,1]])

def roundPoints(strat1, strat2):
    points1 = game_array[strat1, strat2]
    points2 = game_array[strat2, strat1]
    return (points1, points2)


def run_championship(strat_list):
    nstrats = len(strat_list)
    pairings = list(pairs(range(nstrats)))
    npairings = len(pairings)
    global_history = np.zeros((number_of_rounds, npairings, 2))
    for round in range(number_of_rounds):
        for i, p in enumerate(pairings):
            idx1 = p[0]
            idx2 = p[1]
            hist1 = global_history[:, i, 0]
            hist2 = global_history[:, i, 1]
            action1 = strat_list[idx1].determine_action(hist1, hist2, round)
            action2 = strat_list[idx2].determine_action(hist2, hist1, round)
            global_history[round,i, 0] = action1
            global_history[round,i, 1] = action2
    return global_history


def main():
    possible_strats = [strats.AlwaysCooperate(),
                       strats.AlwaysDefect(),
                       strats.TitForTat(),
                       strats.TitForTatRand(0.05),
                       strats.TitForTatRand(0.25),
                       strats.TitForTatRand(0.5),
                       strats.TitForTatRand(0.75),
                       strats.TitForTatRand(0.95),
    ]
    results = run_championship(possible_strats)
    print(results)

if __name__ == "__main__":
    main()
