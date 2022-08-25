# 5099 피자 굽기

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))

    queue = []
    cnt = 1
    for _ in range(N):
        shot = lst.pop(0)
        queue.append((cnt,shot))
        cnt += 1

    cml = True
    while cml:
        cheeze = 0
        if len(queue) == 1:
            cml = False

        elif queue[0][1] != 0:
            cheeze = queue[0][1]//2
            queue.append((queue[0][0], cheeze))
            queue.pop(0)

        else: # queue[0][1] == 0
            queue.pop(0)
            if len(lst) != 0:
                cheeze = lst[0]//2
                queue.append((cnt, cheeze))
                lst.pop(0)
                cnt += 1

    print(f'#{tc} {queue[0][0]}')

