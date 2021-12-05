#!/usr/bin/python

import logging
from agent import Agent

class RecursiveAgent(Agent):
    """Agent for the Recursive halving procedure"""
    def __init__(self, config, id):
        super().__init__(config, id)
        
    def cut_halves(self, i, j):
        """Cut a piece into two (approximately) equally-valued halves"""
        left = 0
        right = sum(self.V[i:j])
        for k in range(i + 1, j+1):
            left += self.V[k - 1]
            right -= self.V[k - 1]
            if left >= right:
                return k
