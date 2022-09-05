# BOJ_4179 불
# 다시 풀자.

R, C = map(int, input().split())

Maze = []
for _ in range(R):
    Maze.append(list(input()))

visited = [[0 for _ in range(C)] for _ in range(R)]

J_Queue = []
F_lst = []
J_cnt, F_cnt = 1, 1

for i in range(R):
    for j in range(C):
        if Maze[i][j] == 'J':
            J_Queue.append((i, j))
            visited[i][j] = ('J', J_cnt)
        elif Maze[i][j] == 'F':
            F_lst.append((i, j))
            visited[i][j] = ('F', F_cnt)

out = 0

while J_Queue:
    J_next = J_Queue.pop(0)

    if J_next[0] == 0 or J_next[0] == R-1 or J_next[1] == 0 or J_next[1] == C-1:
        out = 1
        break

    J_cnt += 1
    F_cnt += 1

    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    J_x, J_y = J_next
    F = []

    for F_next in F_lst:
        F_x, F_y = F_next
        for dt in delta:
            dx, dy = dt
            if 0 <= F_x + dx <= R - 1 and 0 <= F_y + dy <= C - 1 and Maze[F_x + dx][F_y + dy] != '#':
                if visited[F_x + dx][F_y + dy] == 0:
                    visited[F_x + dx][F_y + dy] = ('F', F_cnt)
                    F.append((F_x + dx, F_y + dy))
                    # F_available.append((F_x + dx, F_y + dy))
                elif visited[F_x + dx][F_y + dy][0] != 'F':
                    visited[F_x + dx][F_y + dy] = ('F', F_cnt)
                    F.append((F_x + dx, F_y + dy))
                    # F_available.append((F_x + dx, F_y + dy))
    F_lst = F[:]

    for dt in delta:
        if 0 <= J_x + dx <= R - 1 and 0 <= J_y + dy <= C - 1 and visited[J_x + dx][J_y + dy] == 0 and Maze[J_x + dx][J_y + dy] == '.':
            visited[J_x + dx][J_y + dy] = ('J', J_cnt)
            J_Queue.append((J_x + dx, J_y + dy))
            # J_available.append((J_x+dx, J_y+dy))
            # if J_y + dy == 0 or J_y + dy == C - 1 or J_x + dx == 0 or J_x + dx == R - 1:
            #     J_Queue = []
            #     out = 1
            #     break

    # for shoot in list(set(J_available)-set(F_available)):
    #     J_Queue.append(shoot)

if out:
    print(J_cnt)
else:
    print("IMPOSSIBLE")
