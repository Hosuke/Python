"""B-Tree

   B-trees are balanced search trees designed to work well on magnetic
   disks or direct-access secondary storage devices.  B-trees differ
   signigicantly from red-black trees in that B-tree nodes may have
   many children, from a handful to thousands.

"""

from util import torange, downtorange

######################################################################

class BTreeNode:
    def __init__(self, T):
        self.tree = T
        self.key = {} # we use dictionaries for these.
        self.child = {}
        
class BTree:
    pass

######################################################################

def search(x, k, nil=None):
    i = 1
    while i <= x.n and k > x.key[i]:
        i = i + 1
    if i <= x.n and k == x.key[i]:
        return (x, i)
    if x.leaf:
        return nil
    else:
        __disk_read(x.child[i])
        return search(x.child[i], k)

def create(T, t):
    T.t = t
    x = __allocate_node(T)
    x.leaf = True
    x.n = 0
    __disk_write(x)
    T.root = x

def insert(T, k):
    t = T.t
    r = T.root
    if r.n == 2*t - 1:
        s = __allocate_node(T)
        T.root = s
        s.leaf = False
        s.n = 0
        s.child[1] = r
        __split_child(s, 1, r)
        __insert_nonfull(s, k)
    else:
        __insert_nonfull(r, k)

def print_tree(T):
    __print_tree(T.root)
    print

def __print_tree(x):
    for i in torange(1, x.n):
        if not x.leaf:
            __print_tree(x.child[i])
        print x.key[i],
    if not x.leaf:
        __print_tree(x.child[x.n+1])

def show_tree(T):
    """Show the tree as a side ways tree."""
    __show_tree(T.root)

def __show_tree(x, depth=0):
    for i in downtorange(x.n, 1):
        if not x.leaf:
            __show_tree(x.child[i+1], depth+1)
        for j in xrange(depth):
            print " ",
        print x.key[i]
    if not x.leaf:
        __show_tree(x.child[1], depth+1)

######################################################################

def __insert_nonfull(x, k):
    t = x.tree.t
    i = x.n
    if x.leaf:
        while i >= 1 and k < x.key[i]:
            x.key[i+1] = x.key[i]
            i = i - 1
        x.key[i+1] = k
        x.n = x.n + 1
        __disk_write(x)
    else:
        while i >= 1 and k < x.key[i]:
            i = i - 1
        i = i + 1
        __disk_read(x.child[i])
        if x.child[i].n == 2*t-1:
            __split_child(x, i, x.child[i])
            if k > x.key[i]:
                i = i + 1
        __insert_nonfull(x.child[i], k)

def __allocate_node(T):
    return BTreeNode(T)

def __split_child(x, i, y):
    t = x.tree.t
    z = __allocate_node(x.tree)
    z.leaf = y.leaf
    z.n = t - 1
    for j in torange(1, t-1):
        z.key[j] = y.key[j+t]
    if not y.leaf:
        for j in torange(1, t):
            z.child[j] = y.child[j+t]
    y.n = t - 1
    for j in downtorange(x.n+1, i+1):
        x.child[j+1] = x.child[j]
    x.child[i+1] = z
    for j in downtorange(x.n, i):
        x.key[j+1] = x.key[j]
    x.key[i] = y.key[t]
    x.n = x.n + 1
    __disk_write(y)
    __disk_write(z)
    __disk_write(x)

def __disk_read(x):
    __disk_read.count = __disk_read.count + 1
    if VERBOSE_DISK_ACCESS: print "Disk-Read[%d]: "%__disk_read.count, x
__disk_read.count = 0

def __disk_write(x):
    __disk_write.count = __disk_write.count + 1
    if VERBOSE_DISK_ACCESS: print "Disk-Write[%d]:"%__disk_write.count, x
__disk_write.count = 0



######################################################################

VERBOSE_DISK_ACCESS = False
#VERBOSE_DISK_ACCESS = True

def test():
    t = 2
    data = [9,0,8,1,7,2,6,3,5,4] # same as example in notes
    #data = [0,1,2,3,4,5,6,7,8,9]
    #data = [9,8,7,6,5,4,3,2,1,0]
    print "Test specs: t=%d, data="%t, data
    print
    
    T = BTree()
    create(T, t)
    for d in data:
        if not VERBOSE_DISK_ACCESS:
            print "Inserting %d:"%(d),
            insert(T, d)
            print_tree(T)
            print "Side-ways Tree"
            show_tree(T)
            print
        else:
            print "=== Inserting %d =============================" % d
            insert(T, d)
            print "B-Tree:",
            print_tree(T)
            print
            print "Side-ways Tree"
            show_tree(T)
if __name__ == '__main__': test()
