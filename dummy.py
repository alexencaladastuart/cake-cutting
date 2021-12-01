#!/usr/bin/env python

from agent import Agent

class DUMMY:
    """
    Dummy procedure that takes in three agents and ignores their valuations,
    allocating each approximately a third of the cake by area.
    """
    def __init__(self, config):
        self.conf = config
        self.agent = Agent
        pass

    def run(self, agents):
        if (len(agents)) != 3:
            raise ValueError("dummy requires 3 agents, %d provided" % len(agents))
        third = self.conf.num_pieces // 3
        return [range(third),
                range(third, 2 * third),
                range(2 * third, self.conf.num_pieces)]
