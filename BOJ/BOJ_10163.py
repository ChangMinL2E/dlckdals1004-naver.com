# BOJ_10163 색종이
# 42점.

T = int(input())

lst = []
total = []

papers = []
for _ in range(T):
    papers.append(list(map(int, input().split())))

# if T == 1:
#     print(papers[0][3]*papers[0][4])
else:
    for idx in range(len(papers)):
        lst.append([])

    for idx in range(len(lst)):
        l_index = len(lst)-idx-1
        paper = papers[l_index]
        x,y,R1,R2 = paper[0],paper[1],paper[2],paper[3]
        for i in range(R1):
            for j in range(R2):
                if (x+i,y+j) not in total:
                    lst[l_index].append((x+i, y+j))
                    total.append((x+i, y+j))

    for ls in lst:
        print(len(ls))



