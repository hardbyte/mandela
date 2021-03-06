import strats
import numpy as np
import matplotlib.pyplot as pl

number_of_rounds = 1000

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
    global_history = np.zeros((npairings, number_of_rounds, 2))
    for round in range(number_of_rounds):
        for i, p in enumerate(pairings):
            idx1 = p[0]
            idx2 = p[1]
            hist1 = global_history[i, :, 0]
            hist2 = global_history[i, :, 1]
            action1 = strat_list[idx1].determine_action(hist1, hist2, round)
            action2 = strat_list[idx2].determine_action(hist2, hist1, round)
            global_history[i,round, 0] = action1
            global_history[i,round, 1] = action2
    return global_history

def plot_game(global_history, strats):
    x = np.arange(global_history.shape[1])
    fig = pl.figure()
    ax = fig.add_subplot(111)
    pairings = list(pairs(range(len(strats))))
    ylabels = []
    for p in range(global_history.shape[0]):
        label1 = str(strats[pairings[p][0]])
        label2 = str(strats[pairings[p][1]])
        label = label1 + " vs. " + label2
        ylabels.append(label)
        y1 = (global_history[p, :, 0] - 0.5) * 0.5 + p
        y2 = (global_history[p, :, 1] - 0.5) * 0.5 + p
        ax.plot(x,y1, 'r-', x, y2, 'b-')

    ax.set_yticks(np.arange(len(ylabels)))
    ax.set_yticklabels(ylabels)
    pl.show()




def main():
    possible_strats = []
    params = [0, 0.05, 0.25, 0.3, 0.5, 0.75, 0.9, 0.95, 1.0]
    for Strat in strats.all_strategy_classes:
        if Strat.takes_parameter:
            for param in params:
                possible_strats.append(Strat(param))
        else:
            possible_strats.append(Strat())


    results = run_championship(possible_strats)
    plot_game(results, possible_strats)

if __name__ == "__main__":
    main()
