#!/usr/bin/python

import sys

modules = [
    'matrix',
    'binary_heap',
    'greedy_algorithms',
    'binary_search_tree',
    'red_black_tree',
    'b_tree',
    'disjoint_set',
    'disjoint_set_alternative',
    'graph',
    'binomial_heap',
    'fibonacci_heap',
    'minimum_spanning_tree',
    'single_source_shortest_path',
    'all_pairs_shortest_paths',
    'maximum_flow'
    ]

for module in modules: 
    __import__(module)
    print 
    print "**********************************************************************"
    print "Testing module: %s" % module
    print
    print sys.modules[module].__doc__
    print
    sys.modules[module].test()

print 
print "**********************************************************************"
