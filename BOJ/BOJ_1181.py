# BOJ_1181 단어 정렬
# 단어 길이, 같으면 사전순

N = int(input())
lst = list(set([input() for _ in range(N)]))
lst = sorted(lst, key=lambda x: (len(x),x))

for ls in lst:
    print(ls)