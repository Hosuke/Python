"""Disjoint Set (alternative implementation)
"""

class DisjointSets:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] = self.rank[y] + 1


def test():
    dset = DisjointSets()
    items = list('abcde')
    print "Make sets"
    for x in items:
        dset.make_set(x)
    print "List parents"
    for x in items:
        print dset.find_set(x)
    print "Union sets"
    for i in xrange(0,len(items),2):
        if i+1 < len(items):
            dset.union(items[i], items[i+1])
    print "List parents"
    for x in items:
        print dset.find_set(x)

if __name__ == '__main__': test()
