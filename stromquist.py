#!/usr/bin/env python

import logging
from stromquist_agent import StromquistAgent

class Stromquist:
    """
    Implements the Stromquist moving-knives procedure.
    """
    def __init__(self, config):
        self.conf = config
        self.agent = StromquistAgent

    def assign_pieces(self, i, positions, shouter):
        allocation = [[],[],[]]
        sorted_positions = dict(sorted(positions.items(), key=lambda item: item[1]))

        middle_knife = list(sorted_positions.values())[1]

        Left = [x for x in range(i)]
        Middle = [x for x in range(i, middle_knife)]
        Right = [x for x in range(middle_knife, self.conf.num_pieces)]

        MiddleTaken = False

        for agent in sorted_positions:
            if agent == shouter:
                allocation[agent] = Left
            elif not MiddleTaken:
                allocation[agent] = Middle
                MiddleTaken = True
            else:
                allocation[agent] = Right

        return allocation

    def run(self, agents):
        if (len(agents)) != 3:
            raise ValueError("stromquist requires 3 agents, %d provided" % len(agents))

        # Referee sword on the right side of the ith piece
        for i in range(self.conf.num_pieces):
            logging.info(f"------Round {i}------")
            positions = {}
            for agent in agents:
                positions[agent.id] = agent.get_own_knife_position(i)
            for agent in agents:
                if agent.shout_cut(i, positions):
                    shouter = agent.id
                    return self.assign_pieces(i, positions, shouter)
