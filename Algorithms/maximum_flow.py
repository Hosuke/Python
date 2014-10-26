"""Maximum Flow
"""

import array

def ford_fulkerson(V, E, W, s, t):
    flow = {}
    capacity = {}
    for (u,v) in E:
        flow[(u,v)] = 0
        flow[(v,u)] = 0
        capacity[(u,v)] = W[(u,v)]
        if not (v,u) in E:
            capacity[(v,u)] = 0
    path = __find_path(V, capacity, s, t)
    while path != None:
        c = __path_flow(path, capacity)
        for (u,v) in path:
            flow[(u,v)] = flow[(u,v)] + c
            flow[(v,u)] = -flow[(u,v)]
            capacity[(u,v)] = capacity[(u,v)] - c
            capacity[(v,u)] = capacity[(v,u)] + c
        path = __find_path(V, capacity, s, t)
    max_flow = 0
    for u in V:
        if (u,t) in flow:
            max_flow = max_flow + flow[(u,t)]
    return max_flow
            

# Returns the minimum capacity[(u,v)] for each (u,v) in path.
def __path_flow(path, capacity):
    assert(len(path) > 0)
    c = None
    for edge in path:
        x = capacity[(edge)]
        if c == None or x < c:
            c = x
    return c


def __find_path(V, W, s, t):
    WHITE = 1
    BLACK = 2
    GRAY = 4
    color = {}
    parent = {}
    queue = []
    for u in V:
        parent[u] = None
        color[u] = WHITE
    color[s] = GRAY
    queue.append(s)
    queue_head = 0
    while len(queue) > queue_head:
        u = queue[queue_head]
        queue_head = queue_head + 1
        for v in V:
            if (u,v) in W and W[(u,v)] > 0 and color[v] == WHITE:
                color[v] = GRAY
                parent[v] = u
                queue.append(v)
        color[u] = BLACK
        if parent[t] != None:
            break
    if parent[t] == None:
        return None
    path = []
    v = t
    u = parent[v]
    while u != None:
        path.append((u,v))
        v = u
        u = parent[u]
    path.reverse()
    return path

def test():
    V = list('sabcdt')
    WE = [('s','a',8),
          ('s','c',5),
          ('a','c',5),
          ('a','b',2),
          ('c','d',10),
          ('d','b',2),
          ('b','t',8),
          ('d','t',8)]
    E = []
    W = {}
    for (u,v,w) in WE:
        E.append((u,v))
        W[(u,v)] = w

    ############################################################
    print """
    Ford Fulkerson
    """
    flow = ford_fulkerson(V, E, W, 's', 't')
    print "The maximum flow is %d." % (flow)

if __name__ == '__main__': test()
