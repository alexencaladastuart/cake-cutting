#!/usr/bin/python

from agent import Agent

class LastDiminisherAgent(Agent):
    """Agent for the Last Diminisher procedure"""
    def __init__(self, config, id):
        super().__init__(config, id)

    def diminish(self, i, j):
        """Return the new end value for a piece [i, j) or None"""
        current_val = sum(self.V[i:j])
        target_val = sum(self.V) * 1 / self.conf.num_agents
        if current_val - self.V[j - 1] < target_val: # shouldn't diminish
            return None
        for j_dim in reversed(range(i + 1, j)):
            current_val -= self.V[j_dim]
            if current_val < target_val:
                return j_dim + 1 # last j that met target
        return j_dim # i + 1
