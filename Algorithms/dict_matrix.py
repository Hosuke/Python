"""Dictionary Matrix Module

   This module contains operations related to matrices.  These
   functions assume that a matrix is a list of lists.  The number of
   rows in a matrix M should be available through len(M).  Likewise,
   the number of columns should be available through len(M[0]) if
   len(M) > 0.

"""

def create_matrix(N, M, fill_with=0):
    """Create an n-times-m matrix that is filled with fill_with."""
    result = {}
    for i in N:
        result[i] = {}
        for j in M:
            result[i][j] = fill_with
    return result

create = create_matrix
make = create_matrix

def get_dimensions(M):
    """Get the dimensions of matrix M."""
    n = len(M)
    if n == 0:
        return (0,0)
    
    m = len(M[M.keys()[0]])
    return (n,m)

def get_num_rows(M):
    n,m = get_dimensions(M)
    return n

def get_num_cold(M):
    n,m = get_dimensions(M)
    return m

def clone(A):
    C ={}
    for i in A.keys():
        C[i] = {}
        for j in A[i].keys():
            C[i][j] = A[i][j]
    return C

def get_indices(A):
    N = A.keys()
    M = A[N[0]].keys()
    return N, M

def print_matrix(A):
    """Print matrix A

    For example:
    
    [ 0 1 2 ]
    [ 3 4 5 ]
    [ 6 7 8 ]
    """
    n, m = get_dimensions(A)
    if n > 0:
        N, M = get_indices(A)
        maxlen = {}
        for i in N:
            for j in M:
                x = len(str(A[i][j]))
                if not maxlen.has_key(j):
                    maxlen[j] = x
                else:
                    maxlen[j] = max(maxlen[j], x)
        for i in N:
            s = "[ "
            for j in M:
                t = str(A[i][j])
                for k in xrange(maxlen[j]-len(t)):
                    s += " "
                s += t + " "
            s += "]"
            print s


######################################################################
# TEST
def test():
    print "Matrix A"
    A = create_matrix(4, 5)
    n,m = get_dimensions(A)
    print "A is an %dx%d matrix." % (n,m)
    print_matrix(A)
    print
    print "Matrix B"
    B = create_matrix(3, 3)
    n,m = get_dimensions(B)
    B[n/2][m/2] = 'DIRTY'
    print "B is an %dx%d matrix." % (n,m)
    print_matrix(B)
if __name__ == '__main__': test()
