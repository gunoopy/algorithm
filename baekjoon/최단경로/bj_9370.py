#
# 9370. 미확인 도착지
# https://www.acmicpc.net/problem/9370
#

import sys
import heapq

#
# Functions
#

def Dijkstra(G, V, start, g, h) :
    # node : (distance, is_visit)
    costs = [(float('inf'), 0)] * (V+1)

    # node : (distance, vertex, is_visit)
    heap = [(0, start, 0)]
    visit = {g, h}

    while heap :
        dist, vertex, is_visit = heapq.heappop(heap)

        # heap에 들어간 distance가 최종보다 큰 경우 또는 distance는 동일하지만 heap의 visit이 0, 최종은 1인 경우
        if dist > costs[vertex][0] or (dist == costs[vertex][0] and is_visit < costs[vertex][1]) : continue

        for v, d in G[vertex] :
            temp_visit = 1 if visit == {vertex, v} else is_visit
            new_dist = dist + d
            if new_dist < costs[v][0] or (new_dist == costs[v][0] and temp_visit > costs[v][1]):
                costs[v] = (new_dist, temp_visit)
                heapq.heappush(heap, (new_dist, v, temp_visit))

    return costs

#
# Main
#

T = int(sys.stdin.readline())

for _ in range(T) :
    # t : 목적 후보 개수
    V, E, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    G = {i : [] for i in range(1, V+1)}
    candidates = []

    for _ in range(E) :
        v1, v2, d = map(int, sys.stdin.readline().split())
        G[v1].append((v2, d))
        G[v2].append((v1, d))

    for _ in range(t) :
        candidates.append(int(sys.stdin.readline()))

    costs = Dijkstra(G, V, s, g, h)

    for cand in sorted(candidates) :
        if costs[cand][1] : print(cand, end = ' ')
    else : print()
