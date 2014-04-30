from datatypes import Strategy

from sklearn.ensemble import RandomForestClassifier


# Output variable


class MLRandomForest(Strategy):

    # input variable is the M previous choices from both parties
    # output variable is the choice made by the opponent that you want to predict
    M = 10
    clf = RandomForestClassifier(n_estimators=10)

    def determine_action(self, my_moves, their_moves, turn=0):
        if (turn < M):
            return TitForTat(self, my_moves, their_moves, turn)
        else:
            # call trained classifier on last M moves
            return predict_move(self, my_moves[turn-M:turn], their_moves[turn-M:turn])
 

    def predict_move(self, mine, theirs):
        # predict their move means put their data features first
        X = np.zeros(2*M)
        X[0:M] = theirs
        X[M:2*M] = mine
        return clf.predict(X)


    
    def train_classifier(self, training_array):
        """
        training_array is a numpy array of Nstratpairs * N * 2 numpy arrays

        We make a large numpy array that holds the last M choices from player1
        then the last M choices from player2, and the target array has the 
        value that player 1 chose.
        We then swap player1 and player2, to add the value that player 2 chose.

        Returns int: defect = 0, cooperate = 1
        """
        (npair, nround, nres) = training_array.shape;
        nstep = int(nround / M)
        X = np.zeros((2*npair*nstep,2*M))
        Y = np.zeros(2*npair)
        for i, instance in enumerate(training_array):
            for k in range(0,nstep):
# first one way around
                X[nstep*i+2*k,0:M] = instance[k*M:(k+1)*M,0]
                X[nstep*i+2*k,M:2*M] = instance[k*M:(k+1)*M,1]
                Y[nstep*i+2*k] = instance[(k+1)*M,0]
# now the other way around
                X[nstep*i+2*k+1,0:M] = instance[k*M:(k+1)*M,1]
                X[nstep*i+2*k+1,M:2*M] = instance[k*M:(k+1)*M,0]
                Y[nstep*i+2*k+1] = instance[(k+1)*M,1]
        clf = clf.fit(X, Y)
