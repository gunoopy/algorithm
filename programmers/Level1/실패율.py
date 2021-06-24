def solution(N, stages):
    answer = []
    current = len(stages) # 현재 스테이지까지 도달한 사용자 수
    fail = [0] * (N + 1) # 실패율 저장할 리스트

    for i in range(1, N + 1):
        cnt = stages.count(i)
        fail[i] = cnt / current
        current -= cnt
        if current == 0: break

    for idx, _ in sorted(enumerate(fail[1:]), key=lambda x: x[1], reverse=True):
        answer.append(idx + 1)
    return answer


#
# Main (Test)
#

test_N = [5, 4]
test_stages = [[2, 1, 2, 6, 2, 4, 3, 3], [4,4,4,4,4]]

for N, stages in zip(test_N, test_stages) :
    print(solution(N, stages))