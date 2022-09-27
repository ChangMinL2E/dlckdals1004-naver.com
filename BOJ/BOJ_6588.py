# BOJ_6588 골드바흐의 추측 / 수학
# 굳이, 리스트를 만들어줄 필요가 없다. visited 하나로 끝.

# import sys
cml = True

visited = [False] * 1000001
visited[0] = True
visited[1] = True
Primes = []
for i in range(2, 1001):
    if not visited[i]:
        # Primes.append(i)
        for j in range(i+i, 1000001,i):
            if not visited[j]:
                visited[j] = True

while cml:
    n = int(input()) # 두 수의 합
    if n == 0:
        cml = False

    for k in range(3,n//2+1,2):
        if not visited[n-k] and not visited[k]:
            print(f'{n} = {k} + {n-k}')
            break
    # 이럴꺼면 문제에 출력 해달라고 넣지 말지.
    # else:
    #     print("Goldbach's conjecture is wrong.")











