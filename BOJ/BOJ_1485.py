# BOJ_1485 정사각형  
def distance(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)

N = int(input())

for _ in range(N):
    tmp = 0
    lst = [list(map(int,input().split())) for _ in range(4)]
    lst.sort(key=lambda x:(x[0],x[1]))
    if lst.count(lst[0])==4:
        print(0)

    elif abs(distance(lst[0],lst[1])-distance(lst[2],lst[3])) < 1e-5 and abs(distance(lst[0],lst[2])-distance(lst[1],lst[3])) < 1e-5 and abs(distance(lst[0],lst[3])-distance(lst[2],lst[1])) < 1e-5:
        print(1)
    else:
        print(0)






