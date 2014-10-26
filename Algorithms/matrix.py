"""Matrix Module

   This module contains operations related to matrices.  These
   functions assume that a matrix is a list of lists.  The number of
   rows in a matrix M should be available through len(M).  Likewise,
   the number of columns should be available through len(M[0]) if
   len(M) > 0.

"""

def create_matrix(n, m, fill_with=0):
    """Create an n-times-m matrix that is filled with fill_with."""
    result = []
    for i in xrange(n):
        row = []
        for j in xrange(m):
            row.append(fill_with)
        result.append(row)
    return result

create = create_matrix
make = create_matrix

def get_dimensions(M):
    """Get the dimensions of matrix M."""
    n = len(M)
    if n == 0:
        return (0,0)
    m = len(M[0])
    return (n,m)

def get_num_rows(M):
    n,m = get_dimensions(M)
    return n

def get_num_cold(M):
    n,m = get_dimensions(M)
    return m

def clone(M):
    n,m = get_dimensions(M)
    C = make(n,m)
    for i in xrange(n):
        for j in xrange(m):
            C[i][j] = M[i][j]
    return C

def __get_pattern(x, infinity):
    if infinity != None and x == infinity:
        return "oo"
    else:
        return str(x)

def print_matrix(M, infinity=None):
    """Print matrix M

    For example:
    
    [ 0 1 2 ]
    [ 3 4 5 ]
    [ 6 7 8 ]
    """
    
    if len(M) > 0:
        maxlen = {}
        for row in M:
            for j in xrange(len(row)):
                x = len(__get_pattern(row[j], infinity))
                if not maxlen.has_key(j):
                    maxlen[j] = x
                else:
                    maxlen[j] = max(maxlen[j], x)
        for row in M:
            s = "[ "
            for j in xrange(len(row)):
                t = __get_pattern(row[j], infinity)
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
