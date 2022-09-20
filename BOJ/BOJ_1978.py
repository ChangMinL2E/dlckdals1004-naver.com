# BOJ_1978 소수 찾기

lst = []
visited = [False]*2000
visited[0] = True
visited[1] = True
for i in range(2,2000):
    if not visited[i]:
        lst.append(i)
        for j in range(1,2000//i):
            visited[i*j] = True

N = int(input())
input_lst = list(map(int,input().split()))

total = 0
for num in input_lst:
    if num in lst:
        total += 1

print(total)






