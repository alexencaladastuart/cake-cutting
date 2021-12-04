#!/usr/bin/env python

from last_diminisher_agent import LastDiminisherAgent

class LastDiminisher:
    """
    Implements the Last Diminisher procedure.
    """
    def __init__(self, config):
        self.conf = config
        self.agent = LastDiminisherAgent

    def run(self, agents):
        assert(len(agents) >= 2)
        i = 0 # start of remaining cake
        remaining_agents = agents
        allocations = [None] * self.conf.num_agents
        while len(remaining_agents) > 0:
            j = self.conf.num_pieces # one past the end of current piece
            if len(remaining_agents) == 2: # "I cut, you choose"
                agent1 = remaining_agents[0]
                agent2 = remaining_agents[1]
                k = agent1.cut_halves(i, j)
                a, b = agent2.choose_half(i, k, j)
                allocations[agent1.id] = range(a, b)
                allocations[agent2.id] = range(*((k, j) if a == i else (i, k)))
                return allocations
            for agent in remaining_agents:
                dim = agent.diminish(i, j)
                if dim is not None: # first agent should always diminish
                    last_diminisher = agent
                    j = dim
            remaining_agents.remove(last_diminisher)
            allocations[last_diminisher.id] = range(i, j)
            i = j
