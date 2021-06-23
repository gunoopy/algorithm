#
# 1753. 최단경로
# https://www.acmicpc.net/problem/1753
# Dijkstra`s Single-Source Shortest Path Algorithm
# Using Min Heap
#

import sys
import heapq

#
# Functions
#

def Dijkstra(G, start) :
    costs = [float('inf')] * (V + 1)
    costs[start] = 0
    pq = []
    heapq.heappush(pq, (costs[start], start))

    while pq :
        current_cost, current_node = heapq.heappop(pq)

        # 현재 cost가 Heap에 들어간 cost보다 작으면 continue
        if costs[current_node] < current_cost : continue

        for v, w in G[current_node] :
            moved_cost = current_cost + w
            if costs[v] > moved_cost :
                costs[v] = moved_cost
                heapq.heappush(pq, (moved_cost, v))

    return costs


#
# Main
#

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
G = {i : [] for i in range(1, V+1)}

for _ in range(E) :
    v1, v2, w = map(int, sys.stdin.readline().split())
    G[v1].append((v2, w))

result = Dijkstra(G, start)

for x in result[1:] :
    print(x if x != float('inf') else 'INF')
