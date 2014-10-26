"""Binary Heap Module

   A binary heap is represented by a list.  If the heap is not empty,
   then the first item in the list is always the priority item.

   The priority item is defined by the Priority instance.  BinaryHeap
   defaults to MinPriority.  Priority.compare() returns True if the
   first argument is preferred over the second.

"""

######################################################################
# Public

class Priority:
    def compare(self, a, b):
        """True if a has priority over b."""
        pass

class MinPriority (Priority):
    def compare(self, a, b):
        return cmp(a, b) < 0

class MaxPriority (Priority):
    def compare(self, a, b):
        return cmp(a, b) > 0

min_priority = MinPriority()
max_priority = MaxPriority()

class BinaryHeap:
    def __init__(self, priority=None):
        self.priority = priority
        if self.priority == None:
            self.priority = min_priority
        self.storage = []

    def insert(self, x):
        self.storage.append(x)
        self.__sift_up()
        
    def extract(self):
        if self.is_empty():
            return None
        result = self.storage[0]
        last = self.storage.pop()
        if not self.is_empty():
            self.storage[0] = last
            self.__sift_down()
        # else if it's empty, it means we have extracted the last item
        # and last == result.
        return result

    def get_items(self):
        return self.storage

    def is_empty(self):
        return len(self.storage) == 0

    def __parent(self, c):
        if c == 0:
            return 0
        return (c-1)/2

    def __left(self, p):
        return 2*p + 1

    def __right(self, p):
        return 2*p + 2

    def __better(self, a, b):
        return self.priority.compare(self.storage[a], self.storage[b])

    def __swap(self, a, b):
        self.storage[a], self.storage[b] = self.storage[b], self.storage[a]

    def __get_better_child(self, p):
        n = len(self.storage)
        a = self.__left(p)
        b = self.__right(p)
        if a < n and b < n:
            if self.__better(a, b):
                return a
            else:
                return b
        elif a < n:
            return a
        else:
            return p
                

    def __sift_up(self, s=-1):
        if s < 0:
            c = len(self.storage)-1
        else:
            c = s
        p = self.__parent(c)
        while p < c and self.__better(c, p):
            self.__swap(c, p)
            c = p
            p = self.__parent(c)
        return c

    def __sift_down(self, s=0):
        p = s
        c = self.__get_better_child(p)
        while p < c and self.__better(c, p):
            self.__swap(c, p)
            p = c
            c = self.__get_better_child(p)
        return p

######################################################################
# TEST

def test():
    print """

    1. Heap is created (using default Minimum Priority).
    2. Sequence of numbers is inserted into the heap.
    3. Numbers are extracted until the heap is empty.
    
    """
    
    data = [45,13,12,16,9,5]
    heap = BinaryHeap()
    for d in data:
        heap.insert(d)
        print "INSERT %2d:"%(d), heap.get_items()
    while not heap.is_empty():
        d = heap.extract()
        print "EXTRACT %2d:"%(d), heap.get_items()

if __name__ == '__main__': test()
