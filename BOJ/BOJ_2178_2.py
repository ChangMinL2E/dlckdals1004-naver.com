# BOJ_2178 미로 탐색
# 최단거리이므로 BFS

N, M = map(int, input().split())
Maze = []
Maze.append([0] * (M + 2))
for _ in range(N):
    lst = []
    lst.append(0)
    for ele in list(map(int, input())):
        lst.append(ele)
    lst.append(0)
    Maze.append(lst)
Maze.append([0] * (M + 2))

visited = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
# visited index : 0~N+1 0~M+1

visited[1][1] = 1
Queue = [(1, 1)]

cml = True
while cml:
    x, y = Queue[0][0], Queue[0][1]
    delta = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]

    for alpha in delta:
        if visited[alpha[0]][alpha[1]] == 0 and Maze[alpha[0]][alpha[1]] == 1:
            Queue.append(alpha)  # 가야할 인덱스를 추가함.
            visited[alpha[0]][alpha[1]] = visited[x][y] + 1

    if (N, M) in Queue:
        print(visited[N][M])
        cml = False

    Queue.pop(0)
    # if len(Queue) == 0:
    #     print("탈출 불가능")
    #     cml = False
