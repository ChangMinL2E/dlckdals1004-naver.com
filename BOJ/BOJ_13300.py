# BOJ_13300. 방배정

dic = {}

for j in range(1,7):
    for i in range(2):
        dic[(i,j)] = 0

N = list(map(int,input().split())) # [총인원, 한방 배정 가능한 수]

for _ in range(N[0]):
    A = tuple(map(int,input().split()))
    dic[A] += 1

total = 0
for key, value in dic.items():
    if value == 0:
        pass
    elif value <= N[1]:
        total += 1
    elif value%N[1] == 0:
        total += value//N[1]
    else:
        total += value//N[1] + 1

print(total)



