"""Disjoint-Set

    Some applications involve grouping n distinct objects into a
    collection of disjoint sets. Two important operations are then
    finding which set a given object belongs to and uniting the two
    sets.

    This module implements Disjoint-Set Forests.


"""

######################################################################

class DisjointSetNode:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0

# No need make_set as that is done by the DisjointSetNode's
# constructor.

# def make_set(x):
#     x.parent = x
#     x.rank = 0

def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent

def union(x, y):
    link(find_set(x), find_set(y))

def link(x, y):
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank = y.rank + 1

######################################################################
            
def test():
    small = "abcdef"
    big   = "ABCDEF"

    small_list = test_build_list(small)
    big_list = test_build_list(big)

    test_union(small_list)
    test_union(big_list)

    print "Small Letters"
    test_print_parents(small_list)

    print
    print "Big Letters"
    test_print_parents(big_list)

    union(small_list[0], big_list[0])
    print
    print "Unioned Letters"
    test_print_parents(small_list)
    test_print_parents(big_list)

def test_build_list(values):
    result = []
    for v in values:
        result.append(DisjointSetNode(v))
    return result

def test_union(nodes):
    N = len(nodes)
    n = N / 2
    for i in xrange(n-1):
        union(nodes[i+1], nodes[i])
    for i in xrange(n, N-1):
        union(nodes[i], nodes[i+1])
    union(nodes[0], nodes[N-1])
    

def test_print_parents(list_of_nodes):
    for x in list_of_nodes:
        original_parent = x.parent.value
        set_parent = find_set(x)
        after_parent = x.parent.value
        print "Value:", x.value,
        print "OriginalParent:", original_parent,
        print "ParentAfterPathComparession:", after_parent
        
if __name__ == '__main__': test()
