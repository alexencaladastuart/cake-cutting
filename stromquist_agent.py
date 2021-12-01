#!/usr/bin/python

from agent import Agent

class StromquistAgent(Agent):
    """Agent for the Stromquist moving-knives procedure"""
    def __init__(self, config, id):
        super().__init__(config, id)

    # TODO implement strategy for stromquist
    # placeholder return value
    def shout_cut(self, i):
        return False
