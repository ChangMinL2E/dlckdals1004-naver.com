# BOJ_16987_2 계란으로 계란치기 / Backtracking


def Backtracking(k,N): # lst: 때린 리스트를 봐야겠다.
    global maximum
    if k == N:
        total = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                total += 1
        if maximum < total:
            maximum = total

        return

    if eggs[k][0] > 0: # 만약 내가 들고 있는 계란이 깨지지 않았다면,
        for idx in range(N): # 그 다움 순서부터 봤을때,
            if eggs[idx][0] > 0 and idx != k:# and not lst[idx]: # 아직 때리지 않은 계란이 깨지지 않았다면,
                # lst[idx] = 1
                eggs[idx][0] -= eggs[k][1]
                eggs[k][0] -= eggs[idx][1]
                Backtracking(k+1,N)
                # 원복
                eggs[k][0] += eggs[idx][1]
                eggs[idx][0] += eggs[k][1]
                # lst[idx] = 0
        else:
            Backtracking(N,N)
        # else: # 다 쳤는데, 안깨졌음.
        #     Backtracking([0]*N,k+1,N)
    else: # 친 계란이 깨져있다..?
        Backtracking(k+1,N)
        # for idx in range(k+1,N):
            # if eggs[idx][0] > 0: # 오른쪽 계란부터 봐서 안깨져있으면,
            #     Backtracking(idx,N)
        # else: # 만약 끝까지 다 깨져있으면?
        #     Backtracking(N,N) # 바로 결말 슈웃




N = int(input())
eggs = [list(map(int,input().split())) for _ in range(N)]
# eggs.append([0,0])
maximum = 0

Backtracking(0,N)
print(maximum)




