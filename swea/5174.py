# 트리의 서브트리 원소개수 구하기.

for tc in range(1,int(input())+1):
    E, N = map(int,input().split())
    lst = [[0,0] for _ in range(E+2)]
    inputS = list(map(int,input().split()))

    for i in range(0, len(inputS), 2):
        p, c = inputS[i], inputS[i+1]
        if lst[p][0] == 0:
            lst[p][0] = c
        else:
            lst[p][1] = c


    cnt = 0
    Queue = [N]
    while Queue:
        cnt += 1
        parent = Queue.pop(0)
        for child in lst[parent]:
            if child != 0:
                Queue.append(child)

    print(f'#{tc} {cnt}')


