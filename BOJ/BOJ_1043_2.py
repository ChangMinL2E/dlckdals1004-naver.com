# BOJ_1043 결국 부모를 정해서 풀어야겠다.
# problem) 지나간 집합을 못본다. 묶어줘야한다.

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(x,y):
    if x < y:
        rep[find_set(y)] = find_set(x)
    else:
        rep[find_set(x)] = find_set(y)

N, M = map(int,input().split())
InputLst = list(map(int,input().split()))
Lst = [list(map(int,input().split())) for _ in range(M)]
Liers = [0]*(N+1)
Liers[0] = 1
rep = [x for x in range(N+1)]

for i in InputLst[1:]: # 진실을 아는 사람
    Liers[i] = 1

party_cnt = 0
# 일단 부모를 정해주자.
for ls in Lst:
    new_lst = sorted(ls[1:])
    for l in range(len(new_lst)):
        Union(new_lst[0],new_lst[l])

for ls in range(1,N+1):
    rep[ls] = find_set(ls)

for ls in Lst:
    for l in range(1,len(ls)):
        if Liers[ls[l]]: # 진실을 아는 사람이 있으면,
            for k in range(1,len(ls)): # 부모가 진실을 안다.
                Liers[find_set(ls[l])] = 1
            break

for ls in Lst:
    for l in range(1,len(ls)):
        if Liers[rep[ls[l]]]: # 부모가 진실을 알면,
            break
    else:
        party_cnt += 1
print(party_cnt)



