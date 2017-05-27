# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:14:03 2017

@author: Harsh Kevadia
"""

import pydot

(graph,) = pydot.graph_from_dot_file('DTree.dot')
graph.write_png('somefile.png')