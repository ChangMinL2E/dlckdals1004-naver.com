# BOJ_14889 스타트와 링크

def per(team1, team2,k,N):
    global minimum

    if k == N:
        total1 = 0
        total2 = 0

        for idx in range(N // 2):
            for jdx in range(N // 2):
                total1 += Lst[team1[idx]][team1[jdx]]
                total2 += Lst[team2[idx]][team2[jdx]]

        if minimum > abs(total1 - total2):
            minimum = abs(total1-total2)
        return

    if len(team1) != N//2:
        team1.append(k)
        per(team1, team2, k+1, N)
        team1.pop()

    if len(team2) != N//2:
        team2.append(k)
        per(team1, team2, k+1, N)
        team2.pop()




N = int(input())
Lst = [list(map(int,input().split())) for _ in range(N)]
minimum = 1e10

per([],[],0,N)

print(minimum)




