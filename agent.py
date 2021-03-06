#!/usr/bin/python

import random

class Agent:
    """
    Base class for agents in cake-cutting. Records valuations and includes all
    valuation generation functions. Child classes implement agent behavior for
    specific cake-cutting procedures.
    """
    def __init__(self, config, id):
        self.conf = config
        self.id = id
        self.V = [] # value for each of the conf.num_pieces pieces of the cake

    def gen_uniform_valuation(self):
        self.V = [1] * self.conf.num_pieces

    def gen_random_int_valuation(self, a=0, b=1):
        self.V = [round(random.uniform(a, b))
                  for i in range(self.conf.num_pieces)]
    
    def get_value_of_atoms(self, atoms):
        value = 0
        for atom in atoms:
            value += self.V[atom]
        return value
    
    def get_total_cake_value(self):
        return sum(self.V)

    def gen_normalized_float_valuation(self, total=1):
        """Random float valuation that sums to total"""
        V = [random.random() for i in range(self.conf.num_pieces)]
        S = sum(V)
        self.V = [total * i / S for i in V]

    def cut_halves(self, i, j):
        """Cut a piece into two (approximately) equally-valued halves"""
        left = 0
        right = sum(self.V[i:j])
        for k in range(i + 1, j + 1):
            left += self.V[k - 1]
            right -= self.V[k - 1]
            if left >= right:
                return k

    def choose_half(self, i, j, k):
        """Choose the higher-valued of two pieces [i, j) and [j, k)"""
        return (i, j) if sum(self.V[i:j]) >= sum(self.V[j:k]) else (j, k)

    def __repr__(self):
        return "%s(id=%s total_value=%s valuation=%s)" % (
            self.__class__.__name__,
            self.id, sum(self.V), self.V)
