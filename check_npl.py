#!/usr/bin/env python
# -*- coding: utf-8 -*-

# check_npl.py---

# Copyright (C) 2018 John Asplund <jasplund@daltonstate.edu>

# Author: John Asplund <jasplund@daltonstate.edu

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

'''
Check Neighborhood-prime labeling
----------------------

Exhaustively check for all neighborhood-prime labelings on all graphs with
less than 11 vertices. This is done by going through each graph and 
applying all possible labelings until one works or printing that there is 
a graph that does not work. 

All graphs on less than 10 vertices were provided by Brendan McKay at
http://users.cecs.anu.edu.au/~bdm/data/graphs.html
'''

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from math import gcd
import itertools
from functools import reduce

def gen_labelings(n):
    '''
    gen_labelings, generates all labels to attempt with the desired graph

    Arguments:
    ----------
    n: int instance
        number of vertices in the graph

    RETURNS:
    lst: list of tuples instance
        list of all permutations of the number from 1 to n
    '''
    lst = list(itertools.permutations([x+1 for x in range(n)]))
    return lst

#Test to if the labeling is a neighborhood-prime labeling
def is_np_labeling(G,labeling):
    '''
    is_np_labeling, determines if the given labeling is a 
    neighborhood-prime labeling

    Arguments:
    ----------
    G: networkx.Graph() instance
        full graph

    RETURNS:
    found_label: True or False
                Boolean returned depending on whether the labeling
                works or not. 
    '''
    found_label = True
    for v in nx.nodes(G):
        # Turn neighborhood of x into a list.
        new_lst = [lst[x] for x in G.neighbors(v)]
        if len(new_lst) > 1: # Check to see if new list has at least two neighbors.
            # Change found_label to False when the gcd of the neighborhood of v
            # is not 1.
            if reduce(gcd, new_lst) != 1:
                found_label = False
    # Return False if chosen labeling is not a neighborhood-prime labeling and 
    # return True if the labeling is a neighborhood-prime labeling.
    return found_label

if __name__ == "__main__":
    # N represents the number of vertices in the graph.
    for N in range(2,10):
        # Grab the list of graphs with N vertices.
        g1 = nx.read_graph6("graph{}.g6".format(N))
        # Grab all the possible labelings on N vertices.
        lsts = gen_labelings(N)
        # Run this next for loop for each graph in g1.
        for g in g1:
            one_good_lst = False
            for lst in lsts:
                # if we find a labeling that works, get out of the for loop.
                if is_np_labeling(g,lst):
                    one_good_lst = True
                    break
            # If we could not find a good neighborhood-prime labeling, print
            # the graph, the number of vertices, and the number of edges.
            if not one_good_lst:
                print('Graph with {} vertices, {} edges, and no neighborhood-prime labeling.'
                      .format(len(g.edges()),len(g.nodes())))
                fig, ax = plt.subplots(1,1)
                nx.draw_networkx(g, with_labels=True, node_size = 200, node_color='orange',font_size=10,ax=ax)
                plt.axis('off')
                plt.show()

