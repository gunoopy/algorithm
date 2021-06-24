#
# Level1. 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884
#

def solution(left, right):
    '''
    약수의 개수가 홀수인 경우는 제곱수만 존재
    ex) 1, 4, 9, 16, 25, 36 ...
    '''
    total = (right - left + 1) * (left + right) // 2 # sum(left ~ right)

    i = 1
    while i ** 2 <= right :
        power = i ** 2
        if power >= left :
            total -= 2 * power
        i += 1
    return total

#
# Main (Test)
#

test_left = [13, 24]
test_right = [17, 27]

for left, right in zip(test_left, test_right) :
    print(solution(left, right))