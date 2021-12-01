#!/usr/bin/python

# Utility functions

class Params:
    def __init__(self):
        self._init_keys = set(self.__dict__.keys())

    def add(self, k, v):
        self.__dict__[k] = v

    def __repr__(self):
        return "; ".join("%s=%s" % (k, str(self.__dict__[k])) for k in list(self.__dict__.keys()) if k not in self._init_keys)
