#!/usr/bin/python

from agent import Agent

class StromquistAgent(Agent):
    """Agent for the Stromquist moving-knives procedure"""
    def __init__(self, config, id):
        super().__init__(config, id)

    # TODO implement strategy for stromquist
    # placeholder return value
    def shout_cut(self, i, positions):
        sorted_pos = list(positions.values())
        sorted_pos.sort()
        middle_knife = sorted_pos[1]
        my_knife = positions[self.id]

        Left = sum(self.V[:i])
        Middle = sum(self.V[i:middle_knife])
        Right = sum(self.V[middle_knife:])

        if my_knife >= middle_knife:
            if Left >= Right:
                print(f"Agent {self.id} called cut!")
                return True
        
        if my_knife < middle_knife:
            if Left >= Middle:
                print(f"Agent {self.id} called cut!")
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
        print(f"Agent {self.id} positioned their knife at {i+j}")
        return i + j