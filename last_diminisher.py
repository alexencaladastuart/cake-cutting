#!/usr/bin/env python

import copy
import logging
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
        remaining_agents = copy.deepcopy(agents)
        allocations = [None] * self.conf.num_agents
        while len(remaining_agents) > 0:
            j = self.conf.num_pieces # one past the end of current piece
            if len(remaining_agents) == 2: # switch to "I cut, you choose"
                agent1 = remaining_agents[0]
                agent2 = remaining_agents[1]
                logging.info("Two agents, %d and %d, remain" % (agent1.id, agent2.id))
                k = agent1.cut_halves(i, j)
                logging.info("Agent %s cuts (%d, %d) at %d" % (agent1.id, i, j, k))
                a, b = agent2.choose_half(i, k, j)
                c, d = (k, j) if a == i else (i, k)
                logging.info("Agent %s chooses (%d, %d)" % (agent2.id, a, b))
                logging.info("Agent %s receives (%d, %d)" % (agent2.id, c, d))
                allocations[agent2.id] = range(a, b)
                allocations[agent1.id] = range(c, d)
                return allocations
            for agent in remaining_agents:
                dim = agent.diminish(i, j)
                if dim is not None: # first agent should always diminish
                    logging.info("Agent %s diminishes (%d, %d) to (%d, %d)" %
                                 (agent.id, i, j, i, dim))
                    last_diminisher = agent
                    j = dim
            remaining_agents.remove(last_diminisher)
            allocations[last_diminisher.id] = range(i, j)
            logging.info("Agent %s is the last diminisher and receives (%d, %d)" %
                         (last_diminisher.id, i, j))
            i = j
