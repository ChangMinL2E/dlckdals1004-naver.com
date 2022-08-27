# BOJ_2563 색종이

T = int(input())

lst = []
for _ in range(T):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            lst.append((f'{x+i}-{x+i+1}',f'{y+j}-{y+j+1}'))

lst = list(set(lst))
print(len(lst))



