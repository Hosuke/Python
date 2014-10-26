"""Minimum Spanning Trees
"""

from disjoint_set_alternative import DisjointSets
from binary_heap import BinaryHeap, Priority
import fibonacci_heap as heap
import graph
from util import VertexWeight

class MinEdgePriority (Priority):
    def __init__(self, weights):
        self.weights = weights
        
    def compare(self, edge1, edge2):
        return cmp(self.weights[edge1], self.weights[edge2]) < 0

def kruskal(V, E, W):
    ds = DisjointSets()
    min_weight_priority = MinEdgePriority(W)
    heap = BinaryHeap(min_weight_priority)
    A = []
    for v in V:
        ds.make_set(v)
    for e in E:
        heap.insert(e)
    while not heap.is_empty():
        (u,v) = heap.extract()
        if ds.find_set(u) != ds.find_set(v):
            A.append((u, v))
            ds.union(u, v)
    return A

def prim(V, E, W, r):
        
    # initialise adj
    adj = graph.make_adj(V, E)

    # determine appropriate infinity
    max_weight = None
    for (u,v) in E:
        if max_weight == None or max_weight < W[(u,v)]:
            max_weight = W[(u,v)]
    infinity = max_weight + 10

    node = {}
    parent = {}
    inqueue = {}
    for u in V:
        if u == r:
            uw = VertexWeight(u, 0)
        else:
            uw = VertexWeight(u, infinity)
        node[u] = heap.make_node(uw)
        parent[u] = None
    Q = heap.make_heap()
    for u in V:
        heap.insert(Q, node[u])
        inqueue[u] = True
    while not heap.is_empty(Q):
        if DEBUG:
            print "--------------------------------------------------"
            heap.show_heap(Q)
        x = heap.extract(Q)
        u, w = x.key.get_info()
        assert(node[u].key.get_vertex() == u and node[u].key.get_weight() == w)
        inqueue[u] = False
        for v in adj[u]:
            if inqueue[v] and W[(u,v)] < node[v].key.weight:
                parent[v] = u
                heap.decrease_key(Q, node[v], VertexWeight(v, W[(u,v)]))
    return parent

######################################################################

DEBUG = False

def test():
    V = [1,2,3,4,5,6,7,8,9]
    E = [(1,2), (2,3),
         (4,5), (5,6),
         (7,8), (8,9),
         (1,4), (4,7),
         (2,5), (5,8),
         (3,6), (6,9)]
    E_weights = [31, 9, 44, 14, 48, 20,
                 29, 33, 18, 3, 1, 24]
    W = {}
    for i in xrange(len(E)):
        u, v = E[i]
        W[(u,v)] = E_weights[i]
        W[(v,u)] = E_weights[i]

    EE = []
    for (u,v) in E:
        EE.append((u,v))
        EE.append((v,u))
    E = EE

    print "Kruskal's MST"
    A = kruskal(V, E, W)
    __test_show_sum(A, W)

    print "Prim's MST"
    parent = prim(V, E, W, V[0])
    A = []
    for u in V:
        if parent[u] != None:
            v = parent[u]
            A.append((u, v))
    __test_show_sum(A, W)

def __test_show_sum(A, W):
    AA = []
    sum = 0
    for (u,v) in A:
        if u > v:
            u,v = v,u
        AA.append((u,v))
        sum = sum + W[(u,v)]
    AA.sort()
    print "Edges:", AA
    print "Sum:", sum

######################################################################
if __name__ == '__main__': test()
