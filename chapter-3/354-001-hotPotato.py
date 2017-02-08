from Queue import *


def hotPotato(names, number):

    num_queue = Queue()
    names_list = names
    num = number

    for name in names_list:
        num_queue.enqueue(name)
    print(num_queue.items)


    while num_queue.size() > 1:
        for i in range(num):
            num_queue.enqueue(num_queue.dequeue())
        print(num_queue.items, num_queue.dequeue())
    
    print(num_queue.dequeue())


names = ['bill', 'david', 'susan', 'jane', 'kent', 'brad']
number = 7
hotPotato(names, number)
