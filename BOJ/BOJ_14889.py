# BOJ_14889 스타트와 링크 / 백트래킹
# 다시 볼것.

def Backtracking(Lst, k, N, start_score, link_score):
    global minimum

    if k==N:
        if minimum > abs(start_score-link_score):
            minimum = abs(start_score-link_score)
        return

    for idx in range(2):
        score = 0
        if len(Lst[idx]) < N/2:
            Lst[idx].append(k)
            if len(Lst[idx]) >= 2:
                for i in Lst[idx]:
                    score += lst[i][k]
                    score += lst[k][i]
                    if idx == 0:
                        Backtracking(Lst,k+1,N,start_score+score,link_score)
                        Lst[idx].pop()
                    else: # idx == 1:
                        Backtracking(Lst, k + 1, N, start_score, link_score+score)
                        Lst[idx].pop()
            elif 0 < len(Lst[idx])<=2 :
                Backtracking(Lst, k+1, N, start_score,link_score)
                Lst[idx].pop()


N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

minimum = 10000000
teams = [[],[]]
for idx in range(2):
    teams[idx].append(0)
    Backtracking(teams,1,N,0,0)
    teams[idx].pop()

print(minimum)





