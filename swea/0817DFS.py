G = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'E'],
     'D': ['B', 'F'], 'E': ['B', 'C', 'F'], 'F': ['D', 'E', 'G'], 'G': ['F']}


def dfs(v):
    visited = [False] * 7
    ST = []

    print(v)
    visited[ord(v) - ord('A')] = True

    while True:
        for w in G[v]:
            if visited(ord(w) - ord('A')) == False:
                ST.append(v)
                print(w)
                visited[ord(w) - ord('A')] = True
                v = w
        else:
            if len(ST):
                v = ST.pop()
            else:
                break

print(dfs('A'))