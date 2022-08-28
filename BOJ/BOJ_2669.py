# BOJ_2669. 직사각형 합집합 면적 구하기

lst = []

for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            lst.append((f'{i}-{i+1}',f'{j}-{j+1}'))


lst = list(set(lst))
print(len(lst))



