"""Performance Test

   Test the performance of some of the implementations.

"""

import timing
import random

def test():
    test_python_structures()
#    test_heaps()

def test_python_structures():
    num_vertices = 200
    V = []
    for i in xrange(num_vertices):
        V.append(i)
    G1 = {}
    timing.start()
    for u in V:
        for v in V:
            G1[u*len(V)+v] = True
    timing.finish()
    t1 = timing.micro()
    
    G2 = {}
    timing.start()
    for u in V:
        for v in V:
            G2[(u,v)] = True
    timing.finish()
    t2 = timing.micro()
    print "It took %d %d microseconds to insert %d elements into the dictionary."\
          % (t1, t2, num_vertices**2)
    
          
    

def test_heaps():
    import binomial_heap
    import fibonacci_heap
    impl = [binomial_heap, fibonacci_heap]
    data = __get_random_data(1)
    max_problem_size = 1024

    hdrs = []
    for i in impl:
        hdrs.append(i)
        hdrs.append(i)
        hdrs.append(i)

    __print_header(hdrs)
    while len(data) <= max_problem_size:
        print "  %12d" % len(data),
        for i in impl:
            t_insert, t_extract = __test_heap_impl(i, data)
            print "%12d %12d %12d" % (t_insert, t_extract, t_insert+t_extract),
            
        print
        data = data + __get_random_data(len(data))



def __test_heap_impl(heap, data):
    nodes = []
    for d in data:
        nodes.append(heap.make_node(d))
    H = heap.make_heap()
    timing.start()
    for x in nodes:
        heap.insert(H, x)
    timing.finish()
    t_insert = timing.micro()

    timing.start()
    while not heap.is_empty(H):
        heap.extract(H)
    timing.finish()
    t_extract = timing.micro()
    return t_insert, t_extract


def __print_header(impl, problem_size_label="n"):
    print "# %12.12s" % problem_size_label,
    for i in impl:
        print "%12.12s" % i.__name__,
    print
    print "# ============",
    for i in impl:
        print "============",
    print

def __get_random_data(n):
    A = []
    for i in xrange(n):
        A.append(random.random())
    return A
    


if __name__ == '__main__': test()

