#
# 10217. KCM Travel
# https://www.acmicpc.net/problem/10217
# Dijkstra로 실행 시 메모리 초과 -> Dynamic Programming
#

import sys
from heapq import heappush, heappop
INF = float('inf')
input = sys.stdin.readline

#
# Functions
#

'''
def Dijkstra(G, V, M) :
    costs = [(INF, 0)] * (V+1) # (distance, money)
    last = []
    heap = []
    heappush(heap, (1, 0, 0)) # (node, distance, money)

    while heap :
        node, dist, money = heappop(heap)
        if node == V :
            heappush(last, dist)
            continue

        for neighbor, m, d in G[node] :
            new_dist = dist + d
            new_money = money + m
            if new_money <= M and not(new_dist >= costs[neighbor][0] and new_money >= costs[neighbor][1]) :
                heappush(heap, (neighbor, new_dist, new_money))
                costs[neighbor] = (new_dist, new_money)

    print(last[0] if last else 'Poor KCM')
'''

def dynamic(G, V, M, start) :
    # row : vertex, column : money
    costs = [[INF] * (M+1) for _ in range(V+1)]
    costs[start][0] = 0 # 처음 시작하는 비용은 0, 거리는 0

    for money in range(M+1) :
        for destination in range(1, V+1) :
            if costs[destination][money] == INF : continue # money로 destination에 도달할 수 없는 경우

            for adj_node, adj_money, adj_dist in G[destination] :
                new_money = money + adj_money

                if new_money > M : continue # 비용 초과

                costs[adj_node][new_money] = min(costs[adj_node][new_money], costs[destination][money] + adj_dist)

    min_dist = min(costs[V]) # 한정된 money로 갈 수 있는 최소 거리
    print(min_dist if min_dist != INF else 'Poor KCM')


#
# Main
#


t = int(input())

for _ in range(t) :
    V, M, E = map(int, input().split())
    G = {i : [] for i in range(1, V+1)}

    for _ in range(E) :
        s, e, money, d = map(int, input().split())
        G[s].append((e, money, d)) # (node, money, distance)

    # Dijkstra(G, V, M)
    dynamic(G, V, M, 1)