import time

def sumOfn_1(n):

    start = time.time()

    suma = 0
    for i in range(n):
        suma = suma + n

    end = time.time()
    return n, suma, start - end


def sumOfn_2(n):
    """ fast way of sum """
    start = time.time()
    suma = (n * (n+1))/2
    end = time.time()
    return n, suma, start - end

for x in range(1000000, 10000000, 1000000):
    print("Sum-1 of %d is %d required %10.7f seconds" % sumOfn_1(x))

for i in range(1000000, 10000000, 1000000):
    print("Sum-2 of %d is %d required %10.7f seconds" % sumOfn_2(i))

