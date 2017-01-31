import timeit
import random

for i in range(10000, 100001, 5000):
    t = timeit.Timer("random.randrange (%d) in x"%i, "from __main__ import random, x")

    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("{0} {1} {2}".format(i, lst_time, d_time))
