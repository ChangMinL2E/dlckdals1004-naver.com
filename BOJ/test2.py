# 17136. 색종이 붙이기
import sys
# sys.stdin = open('17136.txt', encoding='UTF-8')
input = sys.stdin.readline

from pprint import pprint
#
N = 10
board = [list(map(int, input().split())) for _ in range(N)]
cards = [0] + [5]*5

def check_size(startpoint, cur_size):
    if cards[cur_size] < 1:
        return False
    y, x = startpoint
    for row in range(cur_size):
        for col in range(cur_size):
            if 0<=y+row<N and 0<=x+col<N:
                if board[y+row][x+col] != 1:
                    return False
            else:
                return False
    return True

def solve(res):
    global minV
    if minV < len(res):
        return
    # 다 붙였나
    no_left = 1
    for y in range(N):
        if sum(board[y]) != 0:
            no_left = 0
    if no_left:
        if minV > len(res):
            minV = len(res)
        return

    for sy in range(N):
        for sx in range(N):
            if board[sy][sx] == 1:
                bool = 0
                for size in range(5, 0, -1):
                    if check_size((sy,sx), size):
                        # 붙이기
                        for row in range(size):
                            for col in range(size):
                                board[sy+row][sx+col] = 0
                        cards[size] -= 1
                        # 여기
                        solve(res + [size])
                        # 떼기
                        for row in range(size):
                            for col in range(size):
                                board[sy+row][sx+col] = 1
                        cards[size] += 1
                        bool = 1
                if bool == 0:
                    return
    pass

minV = 10**5
solve([])

if minV == 10**5:
    print(-1)
else:
    print(minV)



