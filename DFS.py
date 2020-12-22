#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 00:14:43 2020

@author: Jack Kim
"""
graph={
       1:[2,3,4],
       2:[5],
       3:[5],
       4:[],
       5:[6,7],
       6:[],
       7:[3],
       }

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w,discovered)
    return discovered

print(recursive_dfs(1))

def iterative_dfs(start_v):
    discovered =[]
    stack=[start_v]
    while stack:
        v = stack.pop()
        print(v)
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(iterative_dfs(1))