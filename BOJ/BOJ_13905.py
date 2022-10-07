# BOJ_13905 세부 / dijkstra

V, E = map(int,input().split())
st, ed = map(int,input().split())

edge = [list(map(int,input().split())) for _ in range(E)]

# def dijkstra():
#     U = []
#     P = [1e10]*(V+1)
#     D = [-1e10]*(V+1)
#     U[st] = 0
#
#     while True:
#         maximum = -1e10
#         for i in range(1,D):



