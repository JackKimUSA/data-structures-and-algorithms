#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 01:57:29 2020

@author: Jack Kim
"""

#
# Basic Concept and Syntax of Python Dictionary
#

sal_info = {'Austin':91185, 'Boston':90171}
print(sal_info)
sal_info['Boston']=95123
print(sal_info)
sal_info['Atlanta']=91234
print(sal_info)
print(len(sal_info))
del sal_info['Atlanta']
print(sal_info)
print(len(sal_info))
sal_info.clear()
print(sal_info)
print(len(sal_info))

sal_info=dict()
print(sal_info)

sal_info = {'Austin':91185, 'Boston':90171, 'Dallas':89999}

if ('Dallas' in sal_info):
    print(sal_info['Dallas'])
else:
    print("not fount")

for location in sal_info:
    print(sal_info[location])

for location in sal_info:
    print(location)


import csv
with open("treeorderssubsetnodupes.csv", mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {}

    for row in reader:
        key = row[0]
        mydict[key]=row[1]
    
sizeOfDi=len(mydict)
print(sizeOfDi)
print(mydict)

print(mydict['205'])
mydict['205']=10
print(mydict['205'])
infile.close()
print('')

#
# Operations and Methods
#

if ('Seattle' not in sal_info):
    sal_info['Seattle'] = 110340
else:
    print("key exists")
print(sal_info)

print(sal_info.get('Dallas',"not found"))
print(sal_info.get('CA',"not found"))
print(sal_info.keys())
print(sal_info.values())

for k, v in sal_info.items():
    print("the key is", k, "the value is", v)

print("City with highest Salary", max(sal_info, key=sal_info.get))
print("City with lowest Salary", min(sal_info, key=sal_info.get))

print(sal_info)
print(sal_info.popitem())
print(sal_info)
print(sorted(sal_info.keys()))
print(sorted(sal_info.values()))
print('')

eng_di = {}
eng_di['solitude'] = ['lone', 'lonely', 'alone']
eng_di['hope'] = ['wish','ambition']
print(eng_di)
eng_di.clear()
print(eng_di)
eng_di={'solitude':[]}
eng_word = ['lone', 'lonely', 'alone']
eng_di['solitude'].append(eng_word[0])
print(eng_di)
eng_di['solitude']=eng_word
print(eng_di)

if (eng_di.get('solitude')):
    for list_item in eng_di['solitude']:
        print(list_item)
else:
    print("word not in dictionary")
    
with open("TreeOrdersSubset.csv", mode='r') as infile:
    reader = csv.reader(infile)
    treeOrders={}
    
    for row in reader:
        key = row[0]
        
        if (key not in treeOrders):
            treeNum = row[1]
            treeOrders[key]=treeNum
        else:
            treeNum=row[1]
            prev_count = treeOrders[key]
            treeOrders[key]= int(prev_count) + int(treeNum)
            
print(treeOrders.items())
    
infile.close()
print('')
#
# Compare Dictionaries with Other Data Structures
# 

# lists
sal_info_keys = ['Austin', "Portland", "Dallas"]
sal_info_values = [91185,110123,89123]
print(sal_info_keys)
print(sal_info_values)

# to convert lists to dictionary
sal_info={}
index=0
for key in sal_info_keys:
    value = sal_info_values[index]
    sal_info[key] = value
    index += 1

print(sal_info)

# tuples
Cities = ('Austin', "Portland", "Dallas")
print(Cities[0])
print(Cities)

citi_info = {'Austin': 81111, 'Dallas': 91345}
print(citi_info['Dallas'])
print(citi_info)

# sets
city_names_set = {'Austin', 'Portland', 'Dallas', 'Austin'}
print(city_names_set)
for set_value in city_names_set:
    print(set_value)
    
#
# Dictionary Comprehension
#
sal_info_keys = ['Austin', "Portland", "Dallas"]
sal_info_values = [91185,110123,89123]
print(sal_info_keys)
print(sal_info_values)

# to convert lists to dictionary
sal_info={}
for key, value in zip(sal_info_keys,sal_info_values):
    sal_info[key] = value

print(sal_info)

sal_info = {sal_info_keys[index]:sal_info_values[index] for index in range(0, len(sal_info_keys)) }

print(sal_info)