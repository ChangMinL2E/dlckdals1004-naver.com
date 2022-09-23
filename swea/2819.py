# swea 2819. 격자판의 숫자 이어 붙이기

def Backtracking(lst,k,S,x_now,y_now):
    if k==7:
        if not S in total_lst:
            total_lst.append(S)
        return

    for dt in delta:
        x,y = x_now+dt[0], y_now+dt[1]
        if 0<=x<4 and 0<=y<4:
            Backtracking(lst,k+1, S+lst[x][y], x,y)


delta = [(0,1),(1,0),(0,-1),(-1,0)]

for tc in range(1,int(input())+1):
    total_lst = []
    Lst = [input().split() for _ in range(4)]
    for i in range(4):
        for j in range(4):
            Backtracking(Lst,1, Lst[i][j],i,j)

    print(f'#{tc} {len(total_lst)}')








