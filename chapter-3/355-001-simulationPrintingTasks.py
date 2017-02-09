"""
Main Simulation Steps

1.  Create a queue of print tasks. Each task will be given a timestamp upon its arrival.
    The queue is empty at start.

2.  For each second (current_second):
        + Does a new print task get created? 
          If so, add it to the queue with the current_second as the timestamp.

        + If the printer is not busy and if a task is waiting.
          - Remove the next task from the print queue and assign it to the printer.
          - Subtract  the timestamp from the current_second to compute the waiting time
            for that task
          - Append the waiting time for that task to a list for later processing
          - Based of the number of pages in the print task, figure out how much time will
            be required.

        + The printer nod does one second of printing if necessary. It also subtracts one
        second from the time required for that task.

        + If the task has been completed, in other words the time required has reached zero,
          the printer is no longer busy.

3. After the simulation is complete, compute the average waiting time from  the list of waiting
   times generated.
"""

# The Printer class will need to track whether is has a current task. If it does, then it is busy
# and the amount of time needed can be computed from the bumber of pages in the task. The constructor 
# will also allow the pages-per-minute setting to be initialized. The tick method decrements the 
# internal timer and sets the printer to idle if the task is completed.

class Printer():
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = sel.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


# The task class will represent a single printing task. When the task is created, a random number
# generator will provide a length from 1 to 20 pages. We have chosen to use the randrange function
# from the random module.

# Each task will also need a timestamp to be used for computing waiting time. This timestamp will 
# represent the time that the task was created and placed in the printer queue. The wait_time
# method can then be used to retrive the amount of time spent in the queue before printing begins.

import random

class Task():
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


# The main simulation implements the algorithm described above. The print_queue object is 
# an instance of our exisitng queue ADT. A boolean helper function, new_print_task, decides
# whether a new printing task has been created. We have again chosen to use the randrange
# function from the random moudle to return a random integer between 1 and 180. Print tasks
# arrive once every 180 seconds. By arbitrarily choosing 180 from the range of random integers,
# we can simulate this random event. The simulation function allows us to set the total time and
# pages per minute for the printer.

import Queue
import Printer
import Task

import random

def simulation(num_seconds, pages_per_minute):

    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    wait_time = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not printer_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

