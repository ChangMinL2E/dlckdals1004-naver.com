# 게임 맵 최단거리 / 다시 풀것

'''
maps	answer
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1
'''

from collections import deque

def solution(maps):
    answer = -1
    
    visited = [[False for _ in range(len(maps[1]))] for _ in range(len(maps[0]))]
    visited[0][0] = True
    queue = deque([(0,0,1)])
    
    while queue:
        z = queue.popleft()
        if z[0] == len(maps[0])-1 and z[1] == len(maps[1])-1:
            answer = z[2]
        
        for dt in [(-1,0),(0,-1),(1,0),(0,1)]:
            dx = dt[0], dy = dt[1]
            if 0<=z[0]+dx<len(maps[0]) and 0<=z[1]+dy<len(maps[1]) and not visited[z[0]+dx][z[1]+dy] and maps[z[0]+dx][z[1]+dy] == 1:
                queue.append((z[0]+dx,z[1]+dy,z[2]+1))
                visited[z[0]+dx][z[1]+dy] = True
    
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))