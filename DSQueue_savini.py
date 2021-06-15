#Jack Savini
#DSQueue class
#3-31-20
#MA/CS
# CS 102 Spring 2020

#This program simulates a line at disney land, in which some people hold fast passes,
#and others do not. It is as great a representation of a python class, as it is a
#good representation of the bourgeois class, forever stomping their fast-pass-affording
#boots over the necks of the proletariat. In this class will be objects to convey the
#queue size, to tell if its empty, to simulate a rider leaving the queue, to simulate
#a line joiner, and to simulate a bourgeois line joiner.

#FYI, I renamed the file to 'the_queue' because otherwise it pointed to a built in
#class
from the_queue import Queue


class DSQueue:

    #I made two queues to represent the two lines
    def __init__(self):
        self.fastq = Queue()
        self.slowq = Queue()

    #This returns the size of both queues combined.
    def size(self):
        return self.fastq.size() + self.slowq.size()

    #This returns a boolean telling whether the queue is empty or not
    def isEmpty(self):
        return self.size() == 0

    #This simulates a park goer riding the ride, meaning someone has left the queue
    def ride(self):
        #This picks from the faster line, aka the fast pass holders
        if self.fastq.size() > 0:
            return self.fastq.dequeue()

        #When those are depleted, it picks from the slower line.
        elif self.slowq.size() > 0:
            return self.slowq.dequeue()

        #If both are empty, it simply returns nothing.
        else:
            return None

    #This represents someone joining the slow line
    def join(self, item):
        return self.slowq.enqueue(item)

    #and this is someone joing the fast pass holders
    def joinfp(self, item):
        return self.fastq.enqueue(item)
