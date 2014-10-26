class VertexWeight:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
    def __cmp__(self, other):
        return cmp(self.weight, other.weight)
    def get_info(self):
        return (self.vertex, self.weight)
    def get_vertex(self):
        return self.vertex
    def get_weight(self):
        return self.weight
    def __str__(self):
        return str((self.vertex, self.weight))

def torange(a, b, step=1):
    return xrange(a, b+1, step)

def downtorange(a, b, step=-1):
    return xrange(a, b-1, step)

def test():
    print "torange:",
    for i in torange(1, 6, 2):
        print i,
    print

    print "downtorange:",
    for i in downtorange(6, 1, -2):
        print i,
    print


if __name__ == '__main__': test()
