#
# Level3. 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162
# 깊이/너비 우선 탐색(DFS/BFS)
#

from collections import deque

def solution(n, computers):
    queue = deque()
    network = [0] * n
    network_num = 1

    for start in range(n) :
        if not network[start] : # 아직 네트워크가 없는 경우
            network[start] = network_num

            # BFS
            queue.appendleft(start)
            while queue :
                node = queue.pop()
                for conneted_node, is_conneted in enumerate(computers[node]) :
                    # conneted & 아직 네트워크가 없는 경우
                    if is_conneted and not network[conneted_node] :
                        network[conneted_node] = network_num
                        queue.appendleft(conneted_node)

            network_num += 1

    return max(network)


#
# Main (Test)
#

test_n = [3, 3]
test_computers = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]

for n, computers in zip(test_n, test_computers) :
    print(solution(n, computers))