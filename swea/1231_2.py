# 부모 대신, 인덱스를 써보자.

def inorder(index):
    if index:
        inorder(Tree[index][0])
        print(lst[index], end='')
        inorder(Tree[index][1])

for tc in range(1,11):
    N = int(input())
    Tree = [[0,0] for _ in range(N+1)] # 각 노드별 자식 노드 인덱스
    lst = [0]*(N+1) # 각 노드별 원소
    for _ in range(N):
        InputLst = input().split()
        if len(InputLst) == 4:
            lst[int(InputLst[0])] = InputLst[1]
            Tree[int(InputLst[0])][0] = int(InputLst[2])
            Tree[int(InputLst[0])][1] = int(InputLst[3])
        elif len(InputLst) == 3:
            lst[int(InputLst[0])] = InputLst[1]
            Tree[int(InputLst[0])][0] = int(InputLst[2])
        else:
            lst[int(InputLst[0])] = InputLst[1]


    print(f'#{tc}', end=' ')
    inorder(1)
    print()


