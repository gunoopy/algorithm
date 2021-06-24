#
# Level1. 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501
# 월간 코드 챌린지 시즌2
#

def solution(absolutes, signs) :
    return sum(map(lambda value, sign : value if sign else -value , absolutes, signs))

#
# Main (Test)
#

test_absolutes = [[4, 7, 12], [1, 2, 3]]
test_signs = [[True, False, True], [False, False, True]]

for absolutes, signs in zip(test_absolutes, test_signs) :
    print(solution(absolutes, signs))