import string

def solution(s, n):
    lower = string.ascii_lowercase # 소문자 26개
    upper = string.ascii_uppercase # 대문자 26개
    result = ''
    mod = len(lower) # 26

    for c in s :
        if c in lower :
            result += lower[(lower.index(c) + n) % mod]
        elif c in upper :
            result += upper[(upper.index(c) + n) % mod]
        else :
            result += c
    return result

#
# Main (Test)
#

test_s = ['AB', 'z', 'a B z']
test_n = [1, 1, 4]

for s, n in zip(test_s, test_n) :
    print(solution(s, n))