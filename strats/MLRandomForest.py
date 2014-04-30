from datatypes import Strategy
from strats import TitForTat
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Output variable


class MLRandomForest(Strategy):

    # input variable is the M previous choices from both parties
    # output variable is the choice made by the opponent that you want to predict
    M = 20
    clf = RandomForestClassifier(n_estimators=30)

    def __init__(self):
        self.train_classifier()

    def determine_action(self, my_moves, their_moves, turn=0):
        initial = TitForTat()
        if (turn < self.M):
            return initial.determine_action(my_moves, their_moves, turn)
        else:
            # call trained classifier on last M moves
            return self.predict_move(my_moves[turn-self.M:turn], their_moves[turn-self.M:turn])
 

    def predict_move(self, mine, theirs):
        # predict their move means put their data features first
        X = np.zeros(2*self.M)
        X[0:self.M] = theirs
        X[self.M:2*self.M] = mine
        return int(self.clf.predict(X)[0])


    
    def train_classifier(self):
        """

        We make a large numpy array that holds the last M choices from player1
        then the last M choices from player2, and the target array has the 
        value that player 1 chose.
        We then swap player1 and player2, to add the value that player 2 chose.

        """
        training_array = np.load("trainingdata.npy");
        (npair, nround, nres) = training_array.shape;
        nstep = int(nround / self.M) - 1
        print nstep, npair, nround, nres
        X = np.zeros((2*npair*nstep,2*self.M))
        Y = np.zeros(2*npair*nstep)
        for i, instance in enumerate(training_array):
            for k in range(0,nstep):
# first one way around
                X[nstep*i+2*k,0:self.M] = instance[k*self.M:(k+1)*self.M,0]
                X[nstep*i+2*k,self.M:2*self.M] = instance[k*self.M:(k+1)*self.M,1]
                Y[nstep*i+2*k] = instance[(k+1)*self.M,0]
# now the other way around
                X[nstep*i+2*k+1,0:self.M] = instance[k*self.M:(k+1)*self.M,1]
                X[nstep*i+2*k+1,self.M:2*self.M] = instance[k*self.M:(k+1)*self.M,0]
                Y[nstep*i+2*k+1] = instance[(k+1)*self.M,1]
        self.clf.fit(X, Y)
        print self.clf.score(X,Y)
