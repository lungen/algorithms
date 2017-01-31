import timeit
from timeit import Timer

pop_zero = Timer('x.pop(0)', 'from __main__ import x')
pop_end = Timer('x.pop()', 'from __main__ import x')

x = list(range(2000000))
print(pop_zero.timeit(number=1000), 'milliseconds')

x = list(range(2000000))
print(pop_end.timeit(number=1000), 'milliseconds')

for i in range(100000, 1000001, 100000):
    x = list(range(i))
    pe = pop_end.timeit(number=1000)
    x = list(range(i))
    pz = pop_zero.timeit(number=1000)

print("for x.pop(): ", pe)
print("for x.pop(0): ", pz)

