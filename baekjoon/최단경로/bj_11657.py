#
# 11657. 타임머신
# https://www.acmicpc.net/problem/11657
#

import sys
INF = float('inf')
#
# Functions
#

def BellmanFord(G, V, start) :
    dists = [INF] * (V+1)
    dists[start] = 0



#
# Main
#

V, E = map(int, sys.stdin.readline().split())
G = {i : [] for i in range(1, V+1)}

for _ in range(E) :
    v1, v2, d = map(int, sys.stdin.readline().split())
    G[v1].append((v2, d))

dists = BellmanFord(G, V, 1)