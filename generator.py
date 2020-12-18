#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 06:13:29 2020

@author: Jack Kim
"""

#
# Build a generator function
#

# function solution
def even_integers_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print(even_integers_generator(10))
print(list(even_integers_generator(10)))

#
# Use a generator expression
#

# list comprehension
#newlist = [ item.upper() for item in collection]

# generator expression
#(item.upper() for item in colloection)

even_integers = (n for n in range(10) if n % 2 == 0)
print(list(even_integers))

# list of mixed format numbers
numbers = [ 7, 22, 4.5, 99.7, '3', '5']

# convert numbers to integers using expression
integers = (int (n) for n in numbers)
print(list(integers))

names_list = ['Jack', 'Kelly', 'Andrew']

uppercase_names = (name.upper() for name in names_list)
print(list(uppercase_names))

reverse_uppercase = (name[::-1] for name in (name.upper() for name in names_list))
print(list(reverse_uppercase))

uppercase_names = (name.upper() for name in names_list)
reverse_uppercase = (name[::-1] for name in uppercase_names)
print(list(reverse_uppercase))

#
# Use a generator object
#
integers = even_integers_generator(10)
print(integers.__next__())
print(integers.__next__())
print(integers.__next__())
print(integers.__next__())
print(integers.__next__())

integers = even_integers_generator(10)
for n in integers:
    print(n)

for n in even_integers_generator(10):
    print(n)


print(max((i for i in range(10))))
print(max(i for i in range(10)))


#
# The @contextmanager decorator
#
from contextlib import contextmanager
@contextmanager

def simple_context_manager(obj):
    try:
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1

class Some_obj(object):
    def __init__(self,arg):
        self.some_property = arg

obj = Some_obj(5)
print(obj.some_property)

with simple_context_manager(obj):
    print(obj.some_property)

print(obj.some_property)

#
# Use the yielded value
#

HEADER = "this is the header \n"
FOOTER = "\nthis is the footer \n"

@contextmanager
def new_log_file(name):
    try:
        logname = name
        f = open(logname, 'w')
        f.write(HEADER)
        yield f
    finally:
        f.write(FOOTER)
        print("logfile created")
        f.close()

with new_log_file('logfile') as file:
    file.write('this is the body')


#
# Coroutines
#
def coroutine_example():
    while True:
        x = yield
        print (x)

c = coroutine_example()
c.__next__()
c.send(10)

def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item,str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print('No Match')
            else:
                print('Not a string')
    except GeneratorExit:
        print(count)

c = counter('Jack')
c.__next__()
c.send('Jack')
c.send('Kim')
c.send(1234)
c.close()

def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.__next__()
        return cr
    return wrap

@coroutine_decorator
def coroutine_example():
    while True:
        x = yield
        print(x)

c = coroutine_example()
c.send('Jack')

