# key를 입력받아 lst에서 일치하는 경우 위치를 return한다.
# 없는 경우에는 return -1

def find2(key):
    pos = 0
    while pos < N:
        if lst[pos] == key:
            return pos
        pos += 1

    return -1


def find(key):
    pos = 0
    while pos < N and lst[pos] < key:
        pos += 1
    if lst[pos] == key:
        return pos

    return -1


# N = 7
#
#
# lst = [4, 9, 11, 23, 2, 19, 7]
# lst = [1,4,7,9,11,19,29]
# print(find(4))  # 0
# print(find(7))  # 6
# print(find(20))  # -1
# print(find(9))  # 1


# binary Search

def find3(key):
    st = 0
    ed = N - 1
    while st <= ed:
        m = (st + ed) // 2
        if lst[m] == key:  # 찾은 경우
            return m
        elif lst[m] < key:  # 앞의 내용을 버릴경우,
            st = m + 1
        else:
            ed = m - 1
    return -1


# N = 7
#
# # lst = [4, 9, 11, 23, 2, 19, 7]
# lst = [1,4,7,9,11,19,29]
# print(find3(4))
# print(find3(7))
# print(find3(20))
# print(find3(9))

N = 5
lst = [64, 25, 10, 22, 11]

# 0번째 [0~N-1] 제일 작은 값을 찾아서 0

# 1번째 [1~N-1]

for phase in range(0, N - 1):
    # lst[phase: N-1] 중 제일 작은 값의 위치를 찾아
    # minV = 0
    # minV = lst[phase]
    minP = phase
    for idx in range(phase + 1, N):
        # if lst[idx] < minV:
        if lst[idx] < lst[minP]:
            # minV = lst[idx]
            minP = idx
    lst[minP], lst[phase] = lst[phase], lst[minP]

print(lst)
