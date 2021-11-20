import numpy as np


class HMM:
    """
    HMM model class
    Args:
        A: State transition matrix
        states: list of states
        emissions: list of observations
        B: Emmision probabilites
    """

    def __init__(self, A, states, emissions, pi, B):
        self.A = A
        self.B = B
        self.states = states
        self.emissions = emissions
        self.pi = pi
        self.N = len(states)
        self.M = len(emissions)
        self.make_states_dict()

    def make_states_dict(self):
        """
        Make dictionary mapping between states and indexes
        """
        self.states_dict = dict(zip(self.states, list(range(self.N))))
        self.emissions_dict = dict(
            zip(self.emissions, list(range(self.M))))

    def viterbi_algorithm(self, seq):
        """
        Function implementing the Viterbi algorithm
        Args:
            seq: Observation sequence (list of observations. must be in the emmissions dict)
        Returns:
            nu: Porbability of the hidden state at time t given an obeservation sequence
            hidden_states_sequence: Most likely state sequence 
        """
        store_it, sl, ans = list(), list(self.states_dict), list()
        store_it.append(self.B[:,self.emissions_dict[seq[0]]] * self.pi), ans.append(sl[np.argmax(self.B[:,self.emissions_dict[seq[0]]] * self.pi)])
        for i in range(len(seq)):
            if (i == len(seq) - 1): continue
            store_it.append(np.max(store_it[i] * self.A * self.B[:,self.emissions_dict[seq[i+1]]], axis=1)), ans.append(sl[np.argmax(np.max(store_it[i] * self.A * self.B[:,self.emissions_dict[seq[i+1]]], axis=1))])
        return ans
            
            
            
            
            
            
            

            
            
            
            
        
