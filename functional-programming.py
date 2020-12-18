#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 01:57:29 2020

@author: Jack Kim
"""
#
# Functions as data, part 1
#
def say_hello(name):
    print(f'Hello {name}')

say_hello_2 = say_hello
say_hello('Jack')

ENVIRONMENT = 'dev'
#ENVIRONMENT = 'prod'

def fetch_data_real():
    print('Doing some very time intensive operations...')

def fetch_data_fake():
    print('Returning fake data')
    return {
        'name': 'Kelly Park',
        'age' : 38
    }

fetch_data=fetch_data_real() if ENVIRONMENT == 'prod' else fetch_data_fake()

data = fetch_data

#
# Functions as data, part 2
#
def double(x):
    return x * 2

def minus_one(x):
    return x - 1

def squared(x):
    return x * x

my_number = 3

my_number = double(my_number)
my_number = minus_one(my_number)
my_number = squared(my_number)

print(my_number)

function_list = [
    double,
    minus_one,
    squared,
]

my_number = 3
for func in function_list:
    my_number = func(my_number)

print(my_number)

#
# Passing functions as arguments
#
def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def combine_2_and_3(func):
    return func(2,3)

print(combine_2_and_3(add))
print(combine_2_and_3(subtract))
print(combine_2_and_3(max))
print(combine_2_and_3(min))

def combine_names(func):
    return  func('Jack', 'Kim')

def append_with_space(str1, str2):
    return f'{str1} {str2}'

def get_government_form_notation(first, last):
    return f'{last.upper()}, {first.upper()}'

print(combine_names(append_with_space))
print(combine_names(get_government_form_notation))

#
# Returning Functions
#
def create_printer():
    def printer():
        print('Hello functional!')
    return printer

my_printer = create_printer()
my_printer()

def double(x):
    return x * 2

def triple(x):
    return x * 3

def quadruple(x):
    return x * 4

radius=5
diameter = double(radius)
print(diameter)


def create_multiplier(a):
    def multiplier(x):
        return x * a

    return multiplier

double_2=create_multiplier(2)
triple_2=create_multiplier(3)
quadruple_2=create_multiplier(4)
print(double_2(5))
print(triple_2(5))
print(quadruple_2(5))

test_d=create_multiplier(2)(5)
print(test_d)


#
# Closure
#
def create_printer_2():
    my_favorite_number = 42

    def printer():
        print(f'My favorite number is {my_favorite_number}')

    return printer

my_printer = create_printer_2()
my_printer()

def create_counter():
    count = 0

    def get_count():
        return count

    def increment():
        nonlocal count
        count += 1

    return (get_count, increment)

get_count, increment = create_counter()
print(get_count())
increment()
increment()
print(get_count())
increment()
increment()
increment()
print(get_count())

#
# Higer-order functions
#
def divide(x,y):
    if y == 0:
        print('Warning: someone is trying to divide by zero')
        return
    return x / y

def divide_2(x,y):
    return x / y

def second_argument_isnt_zero(func):
    def safe_version(*args):
        if args[1] == 0:
            print('Warning: someone is trying to divide by zero')
            return
        return func(*args)
    return safe_version

divide_safe = second_argument_isnt_zero(divide_2)

print(divide_safe(10,2))
print(divide_safe(10,0))

#
# Mapping
#
numbers=[0,1,2,3,4,5,6,7,8,9]
doubled_numbers = []
for number in numbers:
    doubled = number * 2
    doubled_numbers.append(doubled)

print(doubled_numbers)

def double_3(x):
    return x * 2

doubled_numbers_functional=list(map(double_3,numbers))
print(doubled_numbers_functional)

#
# Filtering
#
numbers=[0,1,2,3,4,5,6,7,8,9]

even_numbrers=[]
for x in numbers:
    if (x % 2 == 0):
        even_numbrers.append(x)
print(even_numbrers)

def is_even(x):
    return x % 2 == 0

even_numbrers_functional = list(filter(is_even, numbers))
print(even_numbrers_functional)

#
# Lambdas
#

numbers=[0,1,2,3,4,5,6,7,8,9]

add = lambda x,y : x + y
print(add(2,3))

doubled_numbers = list(map(lambda x: x *2, numbers))
print(doubled_numbers)

def create_multiplier_2(a):
    return lambda x: x * a

double_3= create_multiplier_2(2)
print(double_3(2))

#
# List comprehensions
#

numbers=[0,1,2,3,4,5,6,7,8,9]

doubled = [x * 2 for x in numbers]
print(doubled)

evens = [x for x in numbers if x % 2 == 0]
print(evens)

#
# Reducing
#
from functools import reduce
numbers=[0,1,2,3,4,5,6,7,8,9]

def get_sum(acc,x):
    print(f'acc is {acc}, x is {x}')
    return acc + x

sum = reduce(get_sum, numbers)
print(sum)

sum = reduce(get_sum, numbers,0)
print(sum)

sum = reduce(get_sum, numbers,100)
print(sum)

#
# Combining List Functions
#

employees = [{
    'name' : 'Jack',
    'salary' : 90000,
    'job_title' : 'developer'
}, {
    'name': 'Kelly',
    'salary': 50000,
    'job_title': 'writer'
},{
    'name': 'Andrew',
    'salary': 120000,
    'job_title': 'engineer'
},{
    'name': 'John',
    'salary': 95000,
    'job_title': 'developer'
}]

def is_developer(employee):
    return employee['job_title'] == 'developer'

def is_not_developer(employee):
    return employee['job_title'] != 'developer'

developers = [x for x in employees if is_developer(x)]
#developers = list(filter(is_developer,employees))
print(developers)

def get_salary(employee):
    return employee['salary']

developer_salaries = [get_salary(x) for x in developers]
#developer_salaries = list(map(get_salary,developers))
print(developer_salaries)

def get_sum_2(acc,x):
    return acc + x

total_developer_salaries = reduce(get_sum_2, developer_salaries,0)
print(total_developer_salaries)
average_developer_salary = total_developer_salaries / len(developer_salaries)
print(average_developer_salary)

non_developers = list(filter(is_not_developer,employees))
non_developer_salaries = list(map(get_salary,non_developers))
total_non_developer_salaries = reduce(get_sum_2, non_developer_salaries,0)
average_non_developer_salary = total_non_developer_salaries / len(non_developer_salaries)
print(average_non_developer_salary)

#
# Partial application and currying
#

def add_1(x,y,z):
    return x + y + z

def add_partial(x):
    def add_others(y,z):
        return x + y + z

    return add_others

add_5 = add_partial(5)
print(add_5(6,7))

def add_partial_2(x,y):
    def add_others(z):
        return x + y + z
    return add_others

add_5_and_6 = add_partial_2(5,6)
print(add_5_and_6(7))

def curry_add(x):
    def curry_add_inner(y):
        def curry_add_inner_2(z):
            return x + y + z
        return curry_add_inner_2
    return curry_add_inner

add_5 = curry_add(5)
add_5_and_6 = add_5(6)
print(add_5_and_6(7))
print(curry_add(5)(6)(7))

from functools import partial

add_5 = partial(add_1, 5)
print(add_5(6,7))

#
# Recursion
#
def count_down(x):
    if x < 0:
        print('Done!')
        return
    
    print(x)
    count_down(x - 1)
    
count_down(10)


def count_up(x, maximum):
    if x > maximum:
        print('Done!')
        return

    print(x) # 0 1 2 3 4 5 6 7 8 9 10
    count_up(x + 1, maximum)
    print(x) # 10 9 8 7 6 5 4 3 2 1 0


count_up(0, 10)


