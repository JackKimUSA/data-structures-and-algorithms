#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 01:57:29 2020

@author: Jack Kim
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq

# Min heapq
hq=[]
heapq.heappush(hq,3)
heapq.heappush(hq,2)
heapq.heappush(hq,1)
print(hq)

hq=[3,5,4,1,2]
heapq.heapify(hq)
print(hq)
heapq.heappop(hq)
print(hq)
heapq.heappop(hq)
print(hq)
heapq.heappop(hq)
print(hq)
print('')

# Max heapq
heap_items=[3,5,4,1,2]
min_heap =[3,5,4,1,2]
heapq.heapify(min_heap)
print('Min Heap:', min_heap)
max_heap =[]
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))
    
print('Max Heap:', max_heap)

max_item = heapq.heappop(max_heap)[1]
print(max_item)

# Max heapq
for i in range(len(heap_items)):
    heap_items[i] *= -1
print(heap_items)
heapq.heapify(heap_items)
print(heap_items)
for i in range(len(heap_items)):
    heap_items[i] *= -1
print(heap_items)

# Min heapq
heap_item=[2,7,4,1,8,1]
hq=[]
heapq.heappush(hq,2)
print(hq)
heapq.heappush(hq,7)
print(hq)
heapq.heappush(hq,4)
print(hq)
heapq.heappush(hq,1)
print(hq)
heapq.heappush(hq,8)
print(hq)
heapq.heappush(hq,1)
print(hq)
print('')

# Max heapq
hq=[]
heapq.heappush(hq,-2)
print(hq)
heapq.heappush(hq,-7)
print(hq)
heapq.heappush(hq,-4)
print(hq)
heapq.heappush(hq,-1)
print(hq)
heapq.heappush(hq,-8)
print(hq)
heapq.heappush(hq,-1)
print(hq)
heapq.heappop(hq)
print(hq)
heapq.heappop(hq)
print(hq)
heapq.heappop(hq)
print(hq)
heapq.heappop(hq)
print(hq)
heapq.heappop(hq)
print(hq)