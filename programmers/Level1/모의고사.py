def solution(answers):
    num = len(answers)
    supo1 = [1, 2, 3, 4, 5] * (num // 5 + 1)
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5] * (num // 8 + 1)
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (num // 10 + 1)

    scores = []
    for supo in [supo1, supo2, supo3]:
        scores.append(sum(map(lambda x, y: x == y, answers, supo)))

    maxi = max(scores)
    answer = []
    for i in range(3):
        if scores[i] == maxi: answer.append(i + 1)

    return answer

#
# Main (Test)
#

test_answers = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]

for answers in test_answers :
    print(solution(answers))