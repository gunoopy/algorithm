import sys
from collections import deque


# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 4
stages = [4,4,4,4,4]

current = len(stages)
fail = [0] * (N+1)
answer = []

for i in range(1, N+1) :
    cnt = stages.count(i)
    fail[i] = cnt / current
    current -= cnt
    if current == 0 : break

for idx, _ in sorted(enumerate(fail[1:]), key = lambda x : x[1], reverse = True) :
    answer.append(idx+1)

print(answer)
