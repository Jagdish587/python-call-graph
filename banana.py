#!/usr/bin/env python

from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph.output import GraphvizOutput

import time


class Banana:

    def __init__(self):
        pass

    def eat(self):
        self.secret_function()
        self.chew()
        self.swallow()

    def secret_function(self):
        time.sleep(0.2)

    def chew(self):
        pass

    def swallow(self):
        pass

config = Config(max_depth=1)
graphviz = GraphvizOutput(output_file='filter_max_depth.png')

with PyCallGraph(output=graphviz, config=config):
    banana = Banana()
    banana.eat()