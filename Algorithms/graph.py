"""Graph Module

   Graphs can be represented as adjacency lists or matrices.  In this
   module, the adjacency list approach is taken.  If a matrix graph is
   required, see the matrix module.

   In this module, a graph is simply a set of vertices V and a set of
   edges E.  In python-speak, E is a set of tuples of elements in V.
   This approach is used in preference over a Graph class because some
   algorithms require a mix and match of elements in V and E
   (e.g. strongly connected components).

"""

import sys

WHITE = 1
BLACK = 2
GRAY  = WHITE+BLACK
INFINITY = sys.maxint
NIL = None

def make_adj(V, E):
    """Create an adjacency list using V and E."""
    adj = {}
    for u in V:
        adj[u] = []
    for (u,v) in E:
        adj[u].append(v)
    return adj

def make_inverse_adj(V, E):
    """Create an inversed adjacenct list.
    That is, all edges (u,v) are recorded as (v,u).
    """
    adj = {}
    for (u,v) in E:
        if not adj.has_key(v):
            adj[v] = []
        adj[v].append(u)
    return adj
            
def bfs(V, adj, s):
    color = {}
    d = {}
    p = {}
    for u in V:
        color[u] = WHITE
        d[u] = INFINITY
        p[u] = NIL
    color[s] = GRAY
    d[s] = 0
    Q = [s]
    while len(Q) != 0:
        u = Q[0]
        for v in adj[u]:
            if color[v] == WHITE:
                color[v] = GRAY
                d[v] = d[u] + 1
                p[v] = u
                Q.append(v)
        Q.remove(u)
        color[u] = BLACK
    return (d, p)

def dfs(V, adj):
    class DfsContext: pass
    c = DfsContext()
    c.adj = adj
    c.color = {}
    c.p = {}
    c.d = {}
    c.f = {}
    c.topo = []
    for u in V:
        c.color[u] = WHITE
        c.p[u] = NIL
    c.count = 0
    for u in V:
        if c.color[u] == WHITE:
            __dfs_visit(u, c)
    return c

def __dfs_visit(u, c):
    c.color[u] = GRAY
    c.d[u] = c.count
    c.count = c.count + 1
    for v in c.adj[u]:
        if c.color[v] == WHITE:
            c.p[v] = u
            __dfs_visit(v, c)
    c.color[u] = BLACK
    c.topo.insert(0,u)
    c.f[u] = c.count
    c.count = c.count + 1

def scc(V, E):
    adj = make_adj(V, E)
    c = dfs(V, adj)
    iadj = make_inverse_adj(V, E)
    c = dfs(c.topo, iadj) # c.topo provides the finish order in
                          # reverse.
    S = {}
    for u in V:
        v = __get_super_parent(u, c.p)
        if not S.has_key(v):
            S[v] = []
        S[v].append(u)
    R = []
    for v in S.keys():
        R.append(S[v])
    return R

######################################################################
    
def __get_super_parent(u, p):
    v = u 
    while p[v] != NIL:
        v = p[v]
    return v

        
######################################################################

def test():
    V = [1,2,3,
         4,5,6,
         7,8,9]
    E = [(1,2), (2,3),
         (4,5), (5,6),
         (7,8), (8,9),
         (1,4), (4,7),
         (2,5), (5,8),
         (3,6), (6,9)]

    test_bfs(V, E)
    print
    test_dfs(V, E)

    E = [(1,4),
         (2,3), (2,5),
         (3,6),
         (4,1),
         (5,4), (5,9),
         (6,2),
         (7,8),
         (8,7), (8,5)]

    print
    test_scc(V, E)

    V = ['Dry dishes', 'Rinse soap', 'Scrub with soap', 'Make soap bubbly',
         'Rinse debris', 'Finish dinner', 'Wipe table clean', 'Store dishes']

    E = [
        ('Rinse soap', 'Dry dishes'),
        ('Scrub with soap', 'Rinse soap'),
        ('Make soap bubbly', 'Scrub with soap'),
        ('Rinse debris', 'Scrub with soap'),
        ('Finish dinner', 'Rinse debris'),
        ('Finish dinner', 'Wipe table clean'),
        ('Dry dishes', 'Store dishes')
        ]

    print
    test_topo(V, E)

def test_bfs(V, E):
    print "Breadth First Search"
    print "  V =", V
    print "  E =", E
    adj = make_adj(V, E)
    (d,p) = bfs(V, adj, V[0])
    for u in V:
        print "d[%s]=%s p[%s]=%s"%(u,d[u],u,p[u])

def test_dfs(V, E):
    print "Depth First Search"
    print "  V =", V
    print "  E =", E
    adj = make_adj(V, E)
    c = dfs(V, adj)
    p = c.p
    d = c.d
    f = c.f
    for u in V:
        print "d[%s]=%2d f[%s]=%2d p[%s]=%s"%(u,d[u],u,f[u],u,p[u])
    
def test_topo(V, E):    
    print "Topological Sort"
    print "  V =", V
    print "  E =", E
    adj = make_adj(V, E)
    c = dfs(V, adj)
    i = 1
    for task in c.topo:
        print "Step %2d:"%i, task
        i = i + 1


def test_scc(V, E):
    print "Strongly Connected Components"
    print "  V =", V
    print "  E =", E
    components = scc(V, E)
    for component in components:
        print component


######################################################################
    
#  LocalWords:  def adj cabinate
if __name__ == '__main__': test()
