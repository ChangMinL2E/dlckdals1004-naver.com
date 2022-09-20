# BOJ_2581 소수

lst = []
visited = [False]*20000
visited[0] = True
visited[1] = True
for i in range(2,20000):
    if not visited[i]:
        lst.append(i)
        for j in range(1,20000//i):
            visited[i*j] = True

A = int(input())
B = int(input())

total = 0
n = 1
for num in range(A,B+1):
    if num in lst:
        total += num
        if n:
            minimum = num
            n = 0
if total == 0:
    print(-1)
else:
    print(total)
    print(minimum)














