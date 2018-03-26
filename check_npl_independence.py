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

#Test to if the labeling is a neighborhood-prime labeling
def is_np_labeling(G):
    '''
    is_np_labeling, determines if the given labeling is a 
    neighborhood-prime labeling

    Arguments:
    ----------
    G: networkx.Graph() instance
        full graph

    RETURNS:
    ----------
    return_value: list or False
                If there exists a list that works, then print the list. Otherwise
                print False.
    '''
    
    for list_set in itertools.combinations([x+1 for x in range(18)], r=9):
        found_fake_label = True
        for v in nx.nodes(G):
            combos = list(list_set)
            # Turn neighborhood of x into a list.
            new_lst = [x for x in G.neighbors(v)]
            if len(new_lst) > 1: # Check to see if new list has at least two neighbors.
                # Change found_label to False when not all of the list_set is in the
                # neighborhood of v.
                temp_lst1 = set(x for x in combos)
                temp_lst2 = set(x for x in new_lst)
                inter_temp = list(temp_lst1 & temp_lst2)
                if len(inter_temp)==len(new_lst):
                    found_fake_label = False
                    break
        if found_fake_label:
            return_value = combos
            break
    # Return False if chosen labeling is not a neighborhood-prime labeling and 
    # return True if the labeling is a neighborhood-prime labeling.
    if not found_fake_label:
        return_value = False
    return return_value

if __name__ == "__main__":
    #define the intersection between two lists of lists.
    def intersect_lofl(a,b):
        temp_lst1 = set(tuple(x) for x in a)
        temp_lst2 = set(tuple(x) for x in b)
        temp_inter = temp_lst1 & temp_lst2
        return [list(x) for x in temp_inter]
    
    G=nx.Graph()
    G.add_nodes_from([x+1 for x in range(18)])
    G.add_edges_from([(i,i+1) for i in range(1,18)]+[(18,1)]+\
                      [(3,16),(5,14),(7,12),(4,17),(6,15),(8,13)])
    # If we could not find a good neighborhood-prime labeling, print
    # the False and otherwise, print the partial labeling.
    print(is_np_labeling(G))
