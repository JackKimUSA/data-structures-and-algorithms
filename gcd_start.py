#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 01:57:29 2020

@author: Jack Kim
"""

# Find the GCD(Greastest Common Denominator) of two numbers using Euclid's algorithm

def gcd(a,b):
    while (b!=0):
        t = a
        a = b
        b = t % b

    return a


# try out the function with a few examples
print(gcd(60,96))   # should be 12
print(gcd(20,8))    # should be 4