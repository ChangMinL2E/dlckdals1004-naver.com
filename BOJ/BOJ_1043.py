# BOJ_1043 거짓말

N, M = map(int,input().split())
InputLst = list(map(int,input().split()))
Lst = [list(map(int,input().split())) for _ in range(M)]
Liers = [0]*(N+1)
Liers[0] = 1

for i in InputLst[1:]: # 진실을 아는 사람
    Liers[i] = 1

party_cnt = 0
for ls in Lst:
    for l in range(1,len(ls)):
        if Liers[ls[l]]: # 진실을 아는 사람이 있으면,
            for k in range(1,len(ls)): # 그 파티 참석자들은 진실을 알게 된다.
                Liers[ls[k]] = 1
            break

for ls in Lst:
    for l in range(1,len(ls)):
        if Liers[ls[l]]: # 진실을 아는 사람이 있으면 다음 집합,
            break
    else:
        party_cnt += 1
print(party_cnt)






