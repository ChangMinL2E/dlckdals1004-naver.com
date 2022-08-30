# BOJ_13549 숨바꼭질 3
# 순간이동의 시간이 0초.

visited = [0] * 100001
N, K = map(int, input().split())

Queue = []
visited[N] = 1
Queue.append(N)

cml = True
while cml:
    next_N = Queue.pop(0)
    N1 = next_N - 1
    N2 = next_N + 1
    N3 = next_N * 2
    if 0 <= N1 <= 100000:
        if visited[N1] == 0 or visited[next_N] < visited[N1]:
            visited[N1] = visited[next_N] + 1
            Queue.append(N1)
    if 0 <= N2 <= 100000:
        if visited[N2] == 0 or visited[next_N] < visited[N2]:
            visited[N2] = visited[next_N] + 1
            Queue.append(N2)
    if 0 <= N3 <= 100000:
        if visited[N3] == 0 or visited[next_N] < visited[N3]:
            visited[N3] = visited[next_N]
            Queue.append(N3)

    if visited[K] != 0:
        print(visited[K] - 1)
        cml = False
