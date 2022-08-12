# 찾으면 패턴의 시작위치를 return 하고
# 못 찾으면 -1을 return

# def find(t, p):
#     i = 0
#     j = 0
#     while j < M and i < N: # j가 전부 맞았거나, i(인덱스)가 길이를 벗어난다면 그만!.
#         if t[i] != p[j]: # 비교하다가 다른경우,
#             i = i - j # i는 다시 시작점으로 와주세요.
#             j = -1 # j는 0부터 시작할껀데, 코드를 복잡하게 하지않기 위해 -1로 선언하겠습니다.
#         i = i + 1 # i는 다음 인덱스부터 시작하겠습니다.
#         j = j + 1 # j는 처음부터 다시 비교해보겠습니다.
#     if j == M:
#         return i
#     else:
#         return -1

# 안보고 코딩.

def find(t, p):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == M:
        return i
    else:
        return -1


t = 'a pattern matching algorithm test'
p = 'rithm'
N = len(t)
M = len(p)

print(find(t, p))
