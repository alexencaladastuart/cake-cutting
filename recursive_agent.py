#!/usr/bin/python

import logging
from agent import Agent

class RecursiveAgent(Agent):
    """Agent for the Recursive halving procedure"""
    def __init__(self, config, id):
        super().__init__(config, id)
