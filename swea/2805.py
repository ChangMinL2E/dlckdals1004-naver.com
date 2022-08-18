# 2805. 농작물 수확

for tc in range(1,int(input())+1): # test case
    n = int(input())
    Matrix = []
    for _ in range(n): # n x n 배열 생성
        Matrix.append(list(map(int,input())))

    total = 0
    j = 0
    for i in range(n):
        if i > n//2:
            j = n - i - 1
        else:
            j = i

        lst = Matrix[i][n//2-j: n//2+j+1]
        for ls in lst:
            total += ls

    print(f'#{tc} {total}')