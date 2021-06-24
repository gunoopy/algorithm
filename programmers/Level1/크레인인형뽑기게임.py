def solution(board, moves):
    stack = []
    width = len(board)
    cnt = 0 # result
    before = -1 # 이전 인형 종류

    while moves :
        loc = moves.pop(0)
        loc -= 1
        for i in range(width) :
            if board[i][loc] :
                if before == board[i][loc] :
                    stack.pop()
                    cnt += 2
                    before = stack[-1] if stack else -1
                else :
                    stack.append(board[i][loc])
                    before = stack[-1]
                board[i][loc] = 0
                break
    return cnt


#
# Main (Test)
#

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))