#
# 1956. 운동
# https://www.acmicpc.net/problem/1956
#

import sys

input = sys.stdin.readline

#
# Functions
#

#
# Main
#

V, E = map(int, input().split())
G = {i : [] for i in range(1, V+1)}

for _ in range(E) :
    v1, v2, d = map(int, input().split())