"""Single Source Shortest Path
"""

import graph
import fibonacci_heap as heap
from util import VertexWeight

def __relax(u, v, W, d, p):
    if d[v] > d[u] + W[(u,v)]:
        d[v] = d[u] + W[(u,v)]
        p[v] = u

def __initialise_sssp(V, s, infinity):
    d = {}
    p = {}
    d[s] = 0
    p[s] = None
    for v in V:
        if v == s: continue
        d[v] = infinity
        p[v] = None
    return d,p

def dijkstra(V, adj, W, s, infinity):
    d,p = __initialise_sssp(V, s, infinity)
    S = []
    node = {}
    Q = heap.make_heap()
    for u in V:
        node[u] = heap.make_node(VertexWeight(u, d[u]))
        heap.insert(Q, node[u])
    while not heap.is_empty(Q):
        x = heap.extract(Q)
        u = x.key.get_vertex()
        if DEBUG: print "visit", u
        S.append(u)
        for v in adj[u]:
            __relax(u, v, W, d, p)
            heap.decrease_key(Q, node[v], VertexWeight(v, d[v]))
    return (d, p)

def bellman_ford(V, E, W, s, infinity):
    d,p = __initialise_sssp(V, s, infinity)
    for i in xrange(len(V) - 1):
        for (u,v) in E:
            __relax(u, v, W, d, p)
    for (u,v) in E:
        if d[v] > d[u] + W[(u,v)]:
            return False, d, p
    return True, d, p
        
    

######################################################################
DEBUG = False

def test():
    V = [1,2,3,4,5,6,7,8,9]
    E = [(1,2), (2,3),
         (4,5), (5,6),
         (7,8), (8,9),
         (1,4), (4,7),
         (2,5), (5,8),
         (6,3), (6,9)]
    adj = graph.make_adj(V, E)
    E_weight = [5,8,5,3,2,5,
                3,2,2,1,2,2]

    W = {}
    for i in xrange(len(E)):
        W[E[i]] = E_weight[i]

    print """
    First determine a safe value for infinity.  Since the longest path
    should be no longer than using all the edges, we set infinity to
    the sum of all the weights + 1.
    """

    infinity = sum(E_weight) + 1
    print "infinity =", infinity

    print """
    Test Dijkstra's Single Source Shortest Path
    """
    d, p = dijkstra(V, adj, W, V[0], infinity)
    __print_results(d,p,V)

    print """
    Test Bellman Ford's Single Source Shortest path
    """
    no_cycles, d, p = bellman_ford(V, E, W, V[0], infinity)
    if no_cycles:
        __print_results(d,p,V)
    else:
        print "Cycles were found."

def __print_results(d,p,V):
    for u in V:
        print "Vertex %2s: d=%2s, p=%2s" % (u, d[u], p[u])

######################################################################
if __name__ == '__main__':
    test()

######################################################################
