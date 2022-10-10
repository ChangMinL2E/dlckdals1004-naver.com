# BOJ_1074 Z / recursion , divide and conquer
# 수정중

N, r, c = map(int,input().split())

def divide(left,right,row_n,col_n,num):
    if num == 1:
        print(left)
        return

    if r <= row_n:
        right = (right+left)//2
        row_n = row_n//2
    else:
        left = (right+left)//2 + 1
        row_n = row_n+row_n//2
    if c <= col_n:
        right = (right+left)//2
        col_n = col_n//2
    else:
        left = (right+left)//2 + 1
        col_n = col_n // 2+col_n

    divide(left,right,row_n,col_n,num//4)

divide(0,2**(2*N)-1,2**(N-1)-1, 2**(N-1)-1, 2**(2*N))



