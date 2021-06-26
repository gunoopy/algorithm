import sys
from collections import deque

s = "try    hello world"
# s = 'a A a A a A'


answer = ''
i = 0
for c in s :
    answer += c.lower() if i % 2 else c.upper()
    if c == ' ' : i = 0
    else : i += 1

a = ' '.join([''.join([c.lower() if i%2 else c.upper() for i, c in enumerate(word)]) for word in s.split()])

# b = [(i, j) for i in range(10) else 'abc' for j in range(i, 2*i)]

print(answer)