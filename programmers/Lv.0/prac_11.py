# 안전지대

'''
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]	16
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]	13
[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]] 0
'''


def solution(board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1: # 폭탄이라면,
                for i in range(-1,2,1):
                    for j in range(-1,2,1):
                        if 0 <= x+i < len(board) and 0 <= y+j < len(board) and not board[x+i][y+j]:
                            board[x+i][y+j] = 2        
    answer = 0
    for x in range(len(board)):
        answer += board[x].count(0)
    return answer

a = solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
print(a)