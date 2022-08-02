T = int(input())
# T = 1

for tc in range(1,T+1):
    N = int(input())
    lst_1 = []
    lst_2 = []
    for _ in range(N):
        x1,y1,x2,y2,color = map(int,input().split())

        if color == 1:
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    lst_1.append((i,j))
        elif color == 2:
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    lst_2.append((i,j))
        

    print(f'#{tc} {len(set(lst_1)&set(lst_2))}')