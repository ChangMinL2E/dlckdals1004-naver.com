# BOJ_1941 소문난 칠공주 백트래킹 죽여보자고~

def Backtracking(lst, k, N, curSum):
    if N - k + curSum < 4:
        return

    if k == N and curSum >= 4:
        solutions.append(set(visited))
        return

    x1, y1= visited[-1][0],visited[-1][1]

    if k != N:
        for dt in delta:
            if 0<=x1+dt[0]<=4 and 0<=y1+dt[1]<=4 and (x1+dt[0],y1+dt[1]) not in visited:
                    if lst[x1+dt[0]][y1+dt[1]] == 'Y':
                        visited.append((x1+dt[0],y1+dt[1]))
                        Backtracking(lst, k+1, N, curSum)
                        visited.pop()
                    else:
                        visited.append((x1+dt[0],y1+dt[1]))
                        Backtracking(lst, k+1, N, curSum+1)
                        visited.pop()


Matrix = []
for _ in range(5):
    Matrix.append(list(input()))

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = []
solutions = []

for x in range(5):
    for y in range(5):
        if Matrix[x][y] == 'Y':
            visited.append((x,y))
            Backtracking(Matrix, 1, 7, 0)
            visited.pop()
        else: # 'S'
            visited.append((x,y))
            Backtracking(Matrix, 1, 7, 1)
            visited.pop()

print(len(solutions))

