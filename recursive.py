#!/usr/bin/env python

import logging
import statistics
from recursive_agent import RecursiveAgent

class Recursive:
    """
    Implements the Recursive halving procedure.
    """
    def __init__(self, config):
        self.conf = config
        self.agent = RecursiveAgent

    def run(self, agents, allocation = {}, left = 0, right = None):
        if right == None:
            right = self.conf.num_pieces
        
        if len(agents) == 0:
            pass
            
        elif len(agents) == 1:
            allocation[agents[0].id] = [x for x in range(left, right)]
        
        else:
            knife_positions = {}
            for agent in agents:
                knife_positions[agent] = agent.cut_halves(left, right)
            cut = round(statistics.median(knife_positions.values()))
            
            sorted_positions = dict(sorted(knife_positions.items(), key=lambda item: item[1]))
            left_group = []
            right_group = []
            for agent in sorted_positions:
                if knife_positions[agent] < cut:
                    left_group.append(agent)
                elif knife_positions[agent] > cut:
                    right_group.append(agent)
                else:
                    if len(left_group) < len(agents)/2:
                        left_group.append(agent)
                    else:
                        right_group.append(agent)
        
            left_allocation = self.run(left_group, allocation, left, cut)
            right_allocation = self.run(right_group, allocation, cut, right)
            allocation = left_allocation.copy()
            allocation.update(right_allocation)
        
        return allocation
