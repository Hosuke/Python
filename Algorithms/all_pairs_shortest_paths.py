"""All Pairs Shortest Paths
"""

import matrix as matrix

def __special_matrix_multiply(A, B, infinity):
    n, m = matrix.get_dimensions(A)
    C = matrix.make(n,m)
    for i in xrange(n):
        for j in xrange(m):
            C[i][j] = infinity
            for k in xrange(n):
                x = A[i][k] + B[k][j]
                if x < C[i][j]:
                    C[i][j] = x
    return C

def all_pairs_shortest_paths(W, infinity):
    n = matrix.get_num_rows(W)
    D = W
    m = 1
    while m < n-1:
        D = __special_matrix_multiply(D, D, infinity)
        m = 2 * m
    return D
    
def floyd_warshall(W, infinity):
    n = matrix.get_num_rows(W)
    D = matrix.clone(W)
    DD = matrix.make(n,n)
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                DD[i][j] = min(D[i][j], D[i][k] + D[k][j])
        DD, D = D, DD
    return D

######################################################################
def test():
    V = [1,2,3,4]
    WE = [(1,2,5),
          (2,3,1),
          (3,1,8), (3,4,3),
          (4,1,2)]

    print """
    Initial Data
    """
    print "V =", V
    print "WE =", WE

    print """
    Determine safe infinity.  Safe infinity equals sum of all weights
    + 1.
    """
    infinity = 1
    for (u,v,w) in WE:
        infinity = infinity + w
    print "infinity =", infinity

    n = len(V)

    print """
    Original weights.
    """
    
    W = matrix.make(n, n, infinity)
    for (u,v,w) in WE:
        W[u-1][v-1] = w
    for i in xrange(n):
        W[i][i] = 0
    matrix.print_matrix(W, infinity)

    print """
    Repeated squaring
    """
    
    D = all_pairs_shortest_paths(W, infinity)
    matrix.print_matrix(D, infinity)

    print """
    Floyd-Warshall
    """

    D = floyd_warshall(W, infinity)
    matrix.print_matrix(D, infinity)
    


######################################################################
if __name__ == '__main__':
    test()

######################################################################
