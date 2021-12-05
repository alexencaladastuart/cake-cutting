#!/usr/bin/python

import logging
from agent import Agent

class StromquistAgent(Agent):
    """Agent for the Stromquist moving-knives procedure"""
    def __init__(self, config, id):
        super().__init__(config, id)

    def shout_cut(self, i, positions):
        sorted_pos = list(positions.values())
        sorted_pos.sort()
        middle_knife = sorted_pos[1]

        Left = sum(self.V[:i])
        Middle = sum(self.V[i:middle_knife])
        Right = sum(self.V[middle_knife:])

        if Left >= Right and Left >= Middle:
            logging.debug(f"Agent {self.id} called cut!")
            return True
        
        return False

    def get_own_knife_position(self, i):
        cake = self.V[i:]
        totalvalue = sum(cake)
        value = 0
        j = 0
        while value < totalvalue/2:
            value += cake[j]
            j += 1
        logging.debug(f"Agent {self.id} positioned their knife at {i+j}")
        return i + j
