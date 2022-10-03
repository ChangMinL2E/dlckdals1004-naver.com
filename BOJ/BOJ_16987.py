# BOJ_16987 Backtracking / 나중에 이해하고 다시 풀어.

def Backtracking(eggs, k, N, cnt):
    global maximum

    if maximum > visited.count(False) + cnt:
        return

    if k == N:
        if cnt > maximum:
            maximum = cnt
        return


    if len(eggs) == 1: # eggs=[(S1,W1),(S2,W2)] 안깨지고 버틴 달걀이 있다면,
        egg1 = eggs.pop()
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                egg2 = Lst[i]
                new_egg1, new_egg2 = (egg1[0]-egg2[1],egg1[1]),(egg2[0]-egg1[1],egg2[1])
                # 새로운 계란이 살아 있는 경우.
                if new_egg2[0] > 0 and new_egg1[0]<= 0: # 기존 계란을 깨고,
                    Backtracking([new_egg2],k+1,N,cnt+1)
                elif new_egg2[0] > 0 and new_egg1[0] > 0: # 못 깨고,
                    Backtracking([new_egg2],k+1,N,cnt)
                # 새로운 계란이 깨진 경우
                elif new_egg2[0]<=0 and new_egg1[0] <= 0:
                    Backtracking([],k+1,N,cnt+2)
                elif new_egg2[0] <=0 and new_egg1[0]>0:
                    Backtracking([],k+1,N,cnt+1)
                visited[i] = False
    else: # 계란이 없으면?
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                Backtracking([Lst[i]],k+1,N,cnt)
                visited[i] = False


N = int(input()) # egg_count
Lst = [list(map(int,input().split())) for _ in range(N)] # S: 내구력 , W: 무게
maximum = 0
visited = [False]*N

for i in range(N):
    visited[i] = True
    Backtracking([Lst[i]],1,N,0)
    visited[i] = False

print(maximum)