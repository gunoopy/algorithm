#
# 1504. 특정한 최단 경로
# https://www.acmicpc.net/problem/1504
#

import sys
import heapq

#
# Functions
#

def Dijkstra(start) :
    global G
    costs = [float('inf')] * (V + 1)
    costs[start] = 0
    heap = [(0, start)]


    while heap :
        print(costs)
        dist, vertex = heapq.heappop(heap)

        if dist > costs[vertex] : continue

        for v, d in G[vertex] :
            new_dist = dist + d
            if new_dist < costs[v] :
                costs[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    print()
    return costs





#
# Main (Test)
#

V, E = map(int, sys.stdin.readline().split())
G = {x : [] for x in range(1, V+1)}

for _ in range(E) :
    v1, v2, d = map(int, sys.stdin.readline().split())
    G[v1].append((v2, d))
    G[v2].append((v1, d))

v1, v2 = map(int, sys.stdin.readline().split())

# costs
start_1 = Dijkstra(1)
start_v1 = Dijkstra(v1)
start_v2 = Dijkstra(v2)

distance = min(start_1[v1] + start_v1[v2] + start_v2[V], start_1[v2] + start_v2[v1] + start_v1[V])

print(distance if distance != float('inf') else -1)