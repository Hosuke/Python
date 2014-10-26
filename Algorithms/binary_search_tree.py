"""Binary Search Trees

   Each binary search tree node has a parent, left child, right child,
   and a key.  The tree structure is maintained such that, for any
   given node x, all the keys on the left subtree rooted by x.left are
   less than x.key, conversely, all the keys on the right subtree
   rooted by x.right are greater than or equal to x.key.

"""

class BinarySearchTreeNode:
    def __init__(self, key, nil=None):
        self.key = key
        self.parent = nil
        self.left = nil
        self.right = nil

class BinarySearchTree:
    def __init__(self, root, nil=None):
        self.root = root

def inorder_walk(x, action, nil=None):
    if x.left != nil:
        inorder_walk(x.left, action, nil)
    action(x.key)
    if x.right != nil:
        inorder_walk(x.right, action, nil)


def recursive_search(x, k, nil=None):
    if x == nil or k == x.key:
        return x
    if k < x.key:
        return recursive_search(x.left, k, nil)
    else:
        return recursive_search(x.right, k, nil)

def iterative_search(x, k, nil=None):
    while x != nil and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x

def minimum(x, nil=None):
    while x.left != nil:
        x = x.left
    return x

def maximum(x, nil=None):
    while x.right != nil:
        x = x.right
    return x

def successor(x, nil=None):
    if x.right != nil:
        return minimum(x.right, nil)
    y = x.parent
    while y != nil and x == y.right:
        x = y
        y = y.parent
    return y

def insert(T, z, nil=None):
    y = nil
    x = T.root
    while x != nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == nil:
        T.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
    

def delete(T, z, nil=None):
    if z.left == nil or z.right == nil:
        y = z
    else:
        y = successor(z, nil)
    if y.left != nil:
        x = y.left
    else:
        x = y.right
    if x != nil:
        x.parent = y.parent
    if y.parent == nil:
        T.root = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
    if y != z:
        z.key = y.key
    return y

def print_tree(T, nil=None):
    def f(key): print key,
    print "Inorder Tree:", 
    inorder_walk(T.root, f, nil)
    print

######################################################################
# TEST

def test():
    data = [12,6,14,17,15,16,10,2,18,19]
    print "Add data", data, "to tree."
    T = BinarySearchTree(None)
    for d in data:
        insert(T, BinarySearchTreeNode(d))
    print_tree(T)
    print

    key = 14
    print "Search for %d." %key
    node = iterative_search(T.root, key)
    print "Found node with key=%d." % node.key
    suc = successor(node)
    print "Successor of %d is %d." % (node.key, suc.key)
    print "Delete node with key=%d." % (node.key)
    delete(T, node)
    print_tree(T)
    print

    print "Search for maximum."
    node = maximum(T.root)
    print "Found node with key=%d." % node.key
    suc = successor(node)
    if suc == None:
        print "No successor of %d was found." % (node.key)
    else:
        print "Successor of %d is %d." % (node.key, suc.key)
    print "Delete node with key=%d." % (node.key)
    delete(T, node)
    print_tree(T)
    print

    print "Search for minimum."
    node = minimum(T.root)
    print "Found node with key=%d." % node.key
    suc = successor(node)
    if suc == None:
        print "No successor of %d was found." % (node.key)
    else:
        print "Successor of %d is %d." % (node.key, suc.key)
    print "Delete node with key=%d." % (node.key)
    delete(T, node)
    print_tree(T)
    
if __name__ == '__main__': test()
