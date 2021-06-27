#
# 11404. 플로이드
# https://www.acmicpc.net/problem/11404
# Floyd Warshall - All-Source Shortest Path
# O(V^3)
#

import sys
import heapq
INF = float('inf')

#
# Functions
#

def FloydWarshall(costs, V) :
    # moddle : 경유지
    for middle in range(1, V+1) :
        costs[middle][middle] = 0
        for start in range(1, V+1) :
            for end in range(1, V+1) :
                # 기존 path와 경유지를 통한 path 중 작은 값
                costs[start][end] = min(costs[start][end], costs[start][middle] + costs[middle][end])

#
# Main
#

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
costs = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E) :
    s, e, d = map(int, sys.stdin.readline().split())
    costs[s][e] = min(costs[s][e], d)

FloydWarshall(costs, V)

for row in costs[1:] :
    for col in row[1:] :
        print(col if col != INF else 0, end = ' ')
    print()