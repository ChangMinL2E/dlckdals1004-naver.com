# BOJ_2166 다각형의 면적

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
# lst.sort(key=lambda x:(x[0],x[1]))
# print(lst)
lst.append(lst[0])
total = 0

for i in range(N-1):
    total += lst[i][0]*lst[i+1][1]-lst[i+1][0]*lst[i][1]

sol = round((1/2)*abs(total),1)
print((sol/100)*100)




