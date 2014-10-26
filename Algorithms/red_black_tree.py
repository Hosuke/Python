"""Red Black Tree

   A binary search tree becomes less efficient when the tree becomes
   unbalanced.  For instance, if we store a set of numbers in
   increasing order, we get a tree that essentially is a linked list
   with a lot of empty left-child pointers.

"""

import binary_search_tree as bintree


######################################################################
# Constants

UNDEFINED = 0
RED = 10
BLACK = 20

######################################################################
# Data Structures

class RedBlackTreeNode:
    def __init__(self, key, nil, color=UNDEFINED):
        self.key = key
        self.left = nil
        self.right = nil
        self.parent = nil
        self.color = color

class RedBlackTree:
    def __init__(self, root=None):
        self.__init_nil()
        if root == None:
            self.root = self.nil
        else:
            self.root = root

    def __init_nil(self):
        self.nil = RedBlackTreeNode(None, None)
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil
        self.nil.color = BLACK

######################################################################
# Public

def insert(T, x):
    bintree.insert(T, x, T.nil)
    x.color = RED
    while x.parent.color == RED:
        if x.parent == x.parent.parent.left:
            y = x.parent.parent.right
            if y.color == RED:
                x.parent.color = BLACK
                y.color = BLACK
                x.parent.parent.color = RED
                x = x.parent.parent
            else:
                if x == x.parent.right:
                    x = x.parent
                __left_rotate(T, x)
                x.parent.color = BLACK
                x.parent.parent.color = RED
                __right_rotate(T, x.parent.parent)
        else:
            y = x.parent.parent.left
            if y.color == RED:
                x.parent.color = BLACK
                y.color = BLACK
                x.parent.parent.color = RED
                x = x.parent.parent
            else:
                if x == x.parent.left:
                    x = x.parent
                __right_rotate(T, x)
                x.parent.color = BLACK
                x.parent.parent.color = RED
                __left_rotate(T, x.parent.parent)
    T.root.color = BLACK

def delete(T, z):
    if z.left == T.nil or z.right == T.nil:
        y = z
    else:
        y = bintree.successor(z, T.nil)
    if y.left != T.nil:
        x = y.left
    else:
        x = y.right
    x.parent = y.parent
    if y.parent == T.nil:
        T.root = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
    if y != z:
        z.key = y.key
    if y.color == BLACK:
        __delete_fixup(T, x)
    return y

def search(T, k):
    return bintree.iterative_search(T.root, k, T.nil)

######################################################################
# Private

def __delete_fixup(T, x):
    while x != T.root and x.color == BLACK:
        if x == x.parent.left:
            w = x.parent.right
            if w.color == RED:
                w.color = BLACK
                x.parent.color = RED
                __left_rotate(T, x.parent)
                w = x.parent.right
            if w.left.color == BLACK and w.right.color == BLACK:
                w.color = RED
                x = x.parent
            else:
                if w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    __right_rotate(T, w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = BLACK
                w.right.color = BLACK
                __left_rotate(T, x.parent)
                x = T.root
        else:
            w = x.parent.left
            if w.color == RED:
                w.color = BLACK
                x.parent.color = RED
                __right_rotate(T, x.parent)
                w = x.parent.left
            if w.right.color == BLACK and w.left.color == BLACK:
                w.color = RED
                x = x.parent
            else:
                if w.left.color == BLACK:
                    w.right.color = BLACK
                    w.color = RED
                    __left_rotate(T, w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = BLACK
                w.left.color = BLACK
                __right_rotate(T, x.parent)
                x = T.root
    x.color = BLACK


def __left_rotate(T, x):
    y = x.right
    x.right = y.left
    y.left.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    else:
        if x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
    y.left = x
    x.parent = y

def __right_rotate(T, x):
    y = x.left
    x.left = y.right
    y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    else:
        if x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
    y.right = x
    x.parent = y

######################################################################
# TEST

def test():
    data = [12,6,14,17,15,16,10,2,18,19]
    T = RedBlackTree()
    for d in data:
        z = RedBlackTreeNode(d, T.nil)
        insert(T, z)
        print "Insert %2d:"%d,
        bintree.print_tree(T, T.nil)
    for i in xrange(0, len(data), 2):
        test_search_and_delete(T, data[i])

def test_search(T, k):
    print "Searching for %d..."%(k),
    z = search(T, k)
    print z
    print "Node key=%d"%(z.key)
    return z
    
def test_delete(T, z):
    print "Deleting", z
    delete(T, z)
    bintree.print_tree(T, T.nil)

def test_search_and_delete(T, k):
    z = test_search(T, k)
    test_delete(T, z)
if __name__ == '__main__': test()
