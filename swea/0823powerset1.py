'''
# 기본적인 멱집합 구하는 알고리즘

def par(k): # dfs
    if k == N:
        print(result)
        # return
    else:
        result[k] = 0
        par(k+1)

        result[k] = 1
        par(k+1)
        # for i in range(2):
        #     result[k] = i
        #     par(k+1)
        #



lst = [10, 30, 40]
result = [-1] * N
N = 3
par(0)
'''

# Stack2 p.56 연습문제 2번.

'''
def par(k):
    if k == N: # 다 돌았다. dfs
        # print(result)
        sumV = 0
        for i in range(N):
            if result[i] == 1:
                sumV += lst[i]
        if sumV == 10:
            for i in range(N):
                if result[i] == 1:
                    print(lst[i], end='')
            print()
    else:
        result[k] = 0
        par(k+1)

        result[k] = 1
        par(k+1)

lst = [x for x in range(1,11)]
N = 10
result = [-1]*N
par(0)
'''

# 백트래킹

def par(k, curSum):
    if curSum > 10:
        # print('이상',k, result) # k 는 depth를 의미.
        return

    if k == N: # 다 돌았다. dfs
        # sumV = 0
        # for i in range(N):
        #     if result[i] == 1:
        #         sumV += lst[i]
        if curSum == 10:
            for i in range(N):
                if result[i] == 1:
                    print(lst[i], end='')
            print()
    else:
        result[k] = 0
        par(k+1, curSum)

        result[k] = 1
        par(k+1, curSum+lst[k])


lst = [x for x in range(1,11)]
N = 10
result = [-1]*N
par(0, 0)



# 순열도 연습해보자.
'''
def per(k):
    if k == N:
        print(result)
        for i in range(N):
            print(lst[result[i]], end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            per(k + 1)
            visited[i] = False  # 저장한 값이 다른 경우에 지장이 가면 안되므로, 복구


lst = [10, 20, 30]
N = 3
result = [-1] * N
visited = [False] * N
per(0)
'''
# 수업시간에 진행한 순열 알고리즘.

def f(i, N):
      if i == N:  # 순열 완성.
          print(P)
      else:
          for j in range(i, N):   # P[i]에 들어갈 숫자 P[j] 결정.
              P[i], P[j] = P[j], P[i]
              f(i+1, N)
              P[i], P[j] = P[j], P[i]

P = [1,2,3]
f(0, 3)