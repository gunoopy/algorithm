import sys
from collections import deque
'''
a = [100, 200, 300, 100, 200, 300, 100, 200, 300]
target = [100, 300]

print(list(filter(lambda x : a[x] in target, range(len(a)))))
print([i for i, x in enumerate(a) if x in target])'''

import heapq

a = [(9, 100),(4, 200),(8, 300),(2, 400),(4, 100),(1, 600)]
h = []

for x in a :
    heapq.heappush(h, x)

print(h)
heapq.heapify(a)
print(a)


for _ in range(len(h)) :
    print(heapq.heappop(h))

if float('inf') :
    print(float('inf'))