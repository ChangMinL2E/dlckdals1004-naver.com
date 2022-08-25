# Queue 노드의 거리

def BFS(G,v,n): # 그래프 G, 탐색 시작점 v
    global visited
    visited = [0]*(n+1) # 정점의 개수 n
    queue = [] # 큐 생성
    queue.append(v) # 큐에 탐색점 추가
    visited[v] = 0 # 1
    while queue: # 남은 큐가 있을때까지
        t = queue.pop(0) # front 원소
        for i in G[t]: # 경로가 list의 index에 갈 수 있는 경로가 있음.
            if not visited[i]: # 아직 방문하지 않았다면
                queue.append(i) # 가겠다.
                visited[i] = visited[t] + 1 # 몇번째에 갔는지 check


for tc in range(1,int(input())+1):
    V, E = map(int,input().split())
    lst = [[] for _ in range(V+1)]
    for _ in range(E):
        N = list(map(int, input().split()))
        lst[N[0]].append(N[1])
        lst[N[1]].append(N[0])
    st, ed = map(int,input().split())

    BFS(lst, st, V)
    if visited[ed] == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {visited[ed]}')