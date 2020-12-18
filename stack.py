#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 01:57:29 2020

@author: Jack Kim
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        """
        Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is O(1), or constant time, because appending to the end of a list happens
        in constant time
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the last time for the list, which is also the top item of the Stack.

        The runtime here is constant time, because all it does is index to the last time of the list.
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """
        This method returns the last time in the list, which is also the item as the top of the Stack.

        This method runs in constant time because indexing into a list is done in constant time.
        """
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """
        This method returns the length of the list that is representing the Stack.

        This method runs in constant time because finding the length of a list also in constant time.
        """
        return len(self.items)

    def is_empty(self):
        """
        This method returns a Boolean value describing whether or not the Stack is empty.

        Testing for equality happens in constant time.
        """
        # return len(self.items) == 0
        # return not self.items
        return self.items == []

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push('apple')
    print(s)
    s.push('banana')
    s.push('carrot')
    print(s)
    print(s.pop())
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())

def match_symbols(symbol_str):
    symbol_pairs= {
        '(':')',
        '[':']',
        '{':'}',
    }

    openers=symbol_pairs.keys()
    my_stack = Stack()

    index=0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else:    # The symbol is a closer

            # If the Stack is already empty, the symbols are not balanced
            if my_stack.is_empty():
                return False

            # If there are still items in the Stack, check for a mis-match.
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        index += 1

    if my_stack.is_empty():
        return True

    return False    # Stack is not empty so symbols were not balanced

print(match_symbols('([{}])'))
print(match_symbols('(([{}]])'))

def reversed_sting(input_str):
    rev_string=""
    s=Stack()

    for char in input_str:
        s.push(char)

    while not s.is_empty():
        rev_string += s.pop()

    return rev_string

input_str="1234567890"
print(reversed_sting(input_str))

# Using Linked List
class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

class Stack_ADT:
    def __init__(self):
        self.last=None

    def push(self,item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

stack=Stack_ADT()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for _ in range(5):
    print(stack.pop())

