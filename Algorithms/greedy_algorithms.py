"""Greedy Algorithms

   A greedy algorithm always makes the choice that looks the best at
   the moment.  That is, it makes a locally optimal choice in the hope
   that this choice will lead to a globally optimal solution.  For
   some optimization problems, the greedy algorithm does not yield
   optimal solutions but for many problems, it does.

"""

# def greedy_cpu_scheduling(s, f):
#     n = len(s)
#     A = [0]
#     j = 0
#     for i in xrange(1, n-1):
#         if s[i] >= f[j]:
#             A.append(i)
#             j = i
#     return A

######################################################################
# Huffman Example

class HuffmanNode:
    def get_frequency(self):
        return 0
    def __str__(self):
        return str(self.get_frequency())
    def __cmp__(self, other):
        a = self.get_frequency()
        b = other.get_frequency()
        if a < b:
            return -1
        elif a > b:
            return +1
        else:
            return 0

class HuffmanLeafNode(HuffmanNode):
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
    def get_frequency(self):
        return self.frequency
    def get_character(self):
        return self.character
    def set_binary(self, binary='0'):
        self.binary = binary
    def print_tree(self):
        print "CHARACTER: %s, FREQUENCY: %2d, BINARY: %s"%(self.character, self.frequency, self.binary)
    def get_total_bits(self):
        return len(self.binary) * self.frequency

class HuffmanBranchNode(HuffmanNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.frequency = left.get_frequency() + right.get_frequency()
    def get_frequency(self):
        return self.frequency
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def set_binary(self, binary=''):
        self.left.set_binary(binary+'0')
        self.right.set_binary(binary+'1')
    def print_tree(self):
        self.left.print_tree()
        self.right.print_tree()
    def get_total_bits(self):
        return self.left.get_total_bits() + self.right.get_total_bits()

    

def huffman(C):
    """Return a Huffman tree from a list of HuffmanLeafNodes."""
    import binary_heap
    Q = binary_heap.BinaryHeap(binary_heap.min_priority)
    n = len(C)
    for c in C:
        Q.insert(c)
    for i in xrange(n-1):
        if DEBUG:
            print "Items in queue:",
            __list_freq(Q.get_items())
        x = Q.extract()
        if DEBUG:
            print "Items in queue:",
            __list_freq(Q.get_items())
        y = Q.extract()
        z = HuffmanBranchNode(x, y)
        if DEBUG:
            print "Merged %d and %d into %d" %(x.get_frequency(),
                                               y.get_frequency(),
                                               z.get_frequency())
        Q.insert(z)
    root = Q.extract()
    assert(Q.is_empty())
    return root

def __list_freq(C):
    for c in C:
        print c.get_frequency(),
    print
    

######################################################################
# TEST

DEBUG=False
#DEBUG=True

def test():
    data = {'a':45, 'b':13, 'c':12,
            'd':16, 'e':9,  'f':5}
    C = []
    for character in data.keys():
        C.append(HuffmanLeafNode(character, data[character]))
    print "Items in C:",
    __list_freq(C)
    R = huffman(C)
    R.set_binary()
    R.print_tree()
    print "Total bits required:", R.get_total_bits()
if __name__ == '__main__': test()
