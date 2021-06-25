#
# Level3. 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258
# 2020 카카오 인턴십
#

def solution(gems):
    visited = []
    start = 0
    end = len(gems) - 1

    for i, gem in enumerate(gems) :
        if gem not in visited :
            visited.append(gem)
            end = i



    [1, 2, 2, 1, 1, 3, 4, 1]

    answer = [start+1, end+1]
    return answer


#
# Main (Test)
#

test_gems = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
]

for gems in test_gems :
    print(solution(gems))
