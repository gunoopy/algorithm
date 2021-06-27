#
# 11657. 타임머신
# https://www.acmicpc.net/problem/11657
# Bellman-Ford - Single-Source Shortest Path (cover negative weight)
# O(VE)
#

import sys
INF = float('inf')

#
# Functions
#

def BellmanFord(G, V, start) :
    dists = [INF] * (V+1)
    dists[start] = 0

    for i in range(V+1) : # V 번 확인
        for node in range(1, V+1) :
            for neighbor, d in G[node] :
                if dists[node] + d < dists[neighbor] :
                    dists[neighbor] = dists[node] + d
                    if i == V : return False # V 번째에서도 바뀐다면 음수 사이클 존재

    return dists

#
# Main
#

V, E = map(int, sys.stdin.readline().split())
G = {i : [] for i in range(1, V+1)}

for _ in range(E) :
    v1, v2, d = map(int, sys.stdin.readline().split())
    G[v1].append((v2, d))

dists = BellmanFord(G, V, 1)

if dists :
    for x in dists[2:] :
        print(x if x != INF else -1)
else : print(-1)