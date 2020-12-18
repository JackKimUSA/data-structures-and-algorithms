#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 01:57:29 2020

@author: Jack Kim
"""

def countdown(x):
    if x == 0:
        print("done")
        return
    else:
        print(x)
        countdown(x-1)
        print("foo")

countdown(4)

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)

print(power(2,4))
print(power(2,0))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)

print(factorial(5))
print(factorial(0))

def factorial5():
    return 5 * factorial4()
def factorial4():
    return 4 * factorial3()
def factorial3():
    return 3 * factorial2()
def factorial2():
    return 2 * factorial1()
def factorial1():
    return 1

print(factorial5())

# Iterative factorial algorithm
def factorial_1(number):
    total = 1
    for i in range (1, number+1):
        total *= i
    return total
print(factorial_1(5))

def get_list_length(my_list):
    if my_list == []:
        return 0

    return 1 + get_list_length(my_list[1:])

my_list=[1,2,3,4,5,6]
print(get_list_length(my_list))

def a():
    print('Start of a()')
    b()
    print('End of a()')
def b():
    print('Start of b()')
    c()
    print('End of b()')

def c():
    print('Start of c()')
    print('End of c()')

a()

# Recursive Fibonacci
def fib_1(nthNumber):
    if nthNumber == 1 or nthNumber == 2:
        return 1
    else:
        return fib_1(nthNumber - 2) + fib_1(nthNumber -1 )

print(fib_1(10))

# Recursive Fibonacci with Memoization
FIB_CACHE={}
def fib_2(nthNumber):
    if nthNumber in FIB_CACHE:
        return FIB_CACHE[nthNumber]

    if nthNumber == 1 or nthNumber == 2:
        return 1
    else:
        FIB_CACHE[nthNumber] = fib_2(nthNumber - 2) + fib_2(nthNumber -1 )

    return FIB_CACHE[nthNumber]

print(fib_2(10))

import functools
@functools.lru_cache()

def fib_3(nthNumber):
    if nthNumber == 1 or nthNumber == 2:
        return 1
    else:
        return fib_3(nthNumber - 2) + fib_3(nthNumber - 1)

print(fib_3(10))
