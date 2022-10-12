# BOJ_1932 정수 삼각형

# def per(k,N,curSum,idx):
#     global maximum
#
#     if k == N:
#         if curSum > maximum:
#             maximum = curSum
#         return
#
#     for i in [idx,idx+1]:
#         per(k+1,N,curSum+Lst[k][i],i)

N = int(input())
Lst = []
for _ in range(N):
    Lst.append(list(map(int,input().split())))
# maximum = 0
#
# per(1,N,Lst[0][0],0)
#
# print(maximum)
for i in range(1,N):
    for j in range(len(Lst[i])): # 층별 길이
        if j == 0: # 첫번째는
            Lst[i][j] = Lst[i][j]+Lst[i-1][j] # 1층 양쪽에 더해주겠다.
        elif j == len(Lst[i])-1: # 끝자리는
            Lst[i][j] = Lst[i][j] + Lst[i - 1][j-1]  # 1층 양쪽에 더해주겠다.
        else: # 중간은
            Lst[i][j] = max(Lst[i - 1][j - 1], Lst[i - 1][j]) + Lst[i][j]
print(max(Lst[N - 1]))








