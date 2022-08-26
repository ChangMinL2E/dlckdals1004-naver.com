# BOJ_2605 줄 세우기

N = int(input())
lst = []
inp_lst = list(map(int, input().split()))
for idx in range(0, N):
    lst.insert(inp_lst[idx], idx + 1)

lst = lst[::-1]

print(*lst)
