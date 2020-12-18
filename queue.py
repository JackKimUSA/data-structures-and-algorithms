#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 01:57:29 2020

@author: Jack Kim
"""

class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        """
        Takes in an item and inserts that item into the 0th index of the list that is representing the Queue.

        The runtime is O(n), or linear time, because inserting into the 0th index of a list forces all the other
        items in the list to move one index to the right.
        """
        self.items.insert(0,item)

    def dequeue(self):
        """
        Returns and removes the front-most item of the Queue, which is represented by the last item in the list.

        The runtime is O(1), or constant time, because indexing to the end of a list happens in constant time.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
        Returns the last time in the list. which represents the front-most item in the Queue.

        The runtime is constant because we're just indexing to the last item of the list and returning the value
        found there.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the size of the Queue, which is represent by the length of the list.

        The runtime is O(1), or constant time, because we're only returning the length.
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value expressing whether or not the list representing the Queue is empty.

        Runs is constant time, becuase it's only checking for equality.
        """
        return self.items == []

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    q=Queue()
    print(q)
    print(q.is_empty())
    q.enqueue('apple')
    print(q)
    q.enqueue('banana')
    q.enqueue('carrot')
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())

import random

class PrintQueue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def is_empty():
        return self.items == []

class Job:
    def __init__(self):
        self.pages = random.randint(1,11)

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False

class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self,print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:    # Queue is empty
            return "No more jobs to print"

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "Printing complete."
        else:
            return "An error occurred."
