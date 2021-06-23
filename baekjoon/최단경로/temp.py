import sys
from collections import deque
'''
a = [100, 200, 300, 100, 200, 300, 100, 200, 300]
target = [100, 300]

print(list(filter(lambda x : a[x] in target, range(len(a)))))
print([i for i, x in enumerate(a) if x in target])'''

import heapq

a = [1,9,5,4,3]
sorted_list = []

heapq.heapify(a)

while a :
    sorted_list.append(heapq.heappop(a))

print(sorted_list)


'''h = []
heapq.heappush(h, 9)
heapq.heappush(h, 4)
heapq.heappush(h, 5)
heapq.heappush(h, 3)
heapq.heappush(h, 1)

print(h)

print(heapq.heappop(h), h)
print(heapq.heappop(h), h)
print(heapq.heappop(h), h)
print(heapq.heappop(h), h)
print(heapq.heappop(h), h)'''
