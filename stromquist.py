#!/usr/bin/env python

from stromquist_agent import StromquistAgent

class STROMQUIST:
    """
    Implements the Stromquist moving-knives procedure.
    """
    def __init__(self, config):
        self.conf = config
        self.agent = StromquistAgent

    def assign_pieces(self):
        # TODO assign pieces given a stopping point and agent knife positions
        # placeholder return value
        return [range(self.conf.num_pieces), [], []]

    def run(self, agents):
        if (len(agents)) != 3:
            raise ValueError("stromquist requires 3 agents, %d provided" % len(agents))

        # TODO finish implementing procedure
        # referee sword on the right side of the ith piece
        for i in range(self.conf.num_pieces):
            for agent in agents:
                if agent.shout_cut(i):
                    return self.assign_pieces()
        return self.assign_pieces()
