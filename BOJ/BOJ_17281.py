# BOJ_17281 야구
from itertools import permutations

N = int(input())
hitters = [list(map(int,input().split())) for _ in range(N)]
maximum = 0
combs = []
for co in list(permutations([x for x in range(9)],9)):
    if co[3] == 0:
        combs.append(co) # 4번타자가 첫번째 사람이면, combs이다.


def case(comb):
    global maximum

    score = 0
    inning = 0
    sequence = 0
    while N-inning:
        lst = []
        out = 0
        while 3-out:
            Tagoo = hitters[inning][comb[sequence % 9]]
            if Tagoo: # 이닝의 순번인 사람이,
                if Tagoo == 4:
                    score += len(lst)+1
                    lst = []
                else:
                    if len(lst):
                        for idx in range(len(lst)-1,-1,-1):
                            lst[idx] += Tagoo
                            if lst[idx] >= 4:
                                lst.pop(idx)
                                score += 1
                    lst.append(Tagoo)
            else:
                out += 1
            sequence += 1
        inning += 1

    if maximum < score:
        maximum = score

for com in combs:
    case(com)
# case([4,5,6,0,1,2,3,7,8])
print(maximum)
















