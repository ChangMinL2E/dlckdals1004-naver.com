# BOJ__25305 커트라인

N, M = map(int,input().split())
lst = sorted(map(int,input().split()), reverse=True)

print(lst[M-1])



