# BOJ_9095 1,2,3 더하기

def per(N):
    global cnt

    if N == 0:
        cnt += 1
        return

    if N >= 3:
        per(N-1)
        per(N-2)
        per(N-3)
    elif N ==2:
        per(N-1)
        per(N-2)
    elif N == 1:
        per(N-1)

for _ in range(int(input())):
    cnt = 0
    per(int(input()))
    print(cnt)