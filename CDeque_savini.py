
##Jack Savini
##3-31-20
## Circular Deques
## CS 102 Spring 2020


class Deque:
    def __init__(self, maxsize = 30000):
        self.maxsize = maxsize
        self.items = [None]*maxsize 
        self.front = maxsize - 1   
        self.rear = maxsize -1
        self.size = 0 

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size

    def addRear(self, item):  #version last
        if self.size == self.maxsize:
            print("Queue is Full! Item was not enqueued!")
        else:
            if not self.isEmpty():
                if self.rear == 0:
                    self.rear = self.maxsize - 1
                else:
                    self.rear -= 1
            self.items[ self.rear ] = item
            self.size += 1

    #This class I had to make from scratch. It's basically the same as addRear,
    #onlythings go in the opposite direction cyclically.
    def addFront(self, item):
        #If it's too big then you can't add anything
        if self.size == self.maxsize:
            print("Queue is Full! Item was not enqueued!")
        else:
            if not self.isEmpty():
                #If the selector is already at the front, this takes it to the back
                if self.front == self.maxsize - 1:
                    self.front = 0
                #otherwise it goes forward one
                else:
                    self.front += 1
            #And adds the new item
            self.items[ self.front ] = item
            #thus increasing the size of the queue
            self.size += 1

    def removeFront(self): #version last
        if self.isEmpty():
            print("Queue is Empty! None was returned")
            return None    
        else:
            val = self.items[self.front]
            self.items[self.front] = None
            if self.front != self.rear:
                if self.front == 0:
                    self.front = self.maxsize -1
                else:
                    self.front -= 1
            self.size -= 1
            return val

#this one was also new
    def removeRear(self):
        #If it's empty, it can't get smaller, so a prompt shows up
        if self.isEmpty():
            print("Queue is Empty! None was returned")
            return None    
        else:
            #val is here for the return statement later, to show the number that
            #was erased.
            val = self.items[self.rear]
            #This erases the value
            self.items[self.rear] = None
            #And then moves the pointer for "which number should be erased"
            #forward one
            if self.front != self.rear:
                #This checks if it's already at the end, at which case it will
                #move to the front
                if self.rear == self.maxsize - 1:
                    self.rear = 0
                #otherwise it just goes forward one.
                else:
                    self.rear += 1
            #Of course the size is decreased
            self.size -= 1
            #And the deleted value is returned
            return val


    def __str__(self):
    ## we don't print queues but to see how we did in our design
    ## this let's us see the queue. 
        temp = CQueue()
        stringy = "["
        for a in self.items:
            if a == None:
                stringy += "_"
            else:
                stringy += str(a)
        return stringy+")" + " size =" + str(self.size) + ", f=" + str(self.front) +", r=" + str(self.rear)



