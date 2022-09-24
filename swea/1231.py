# swea 1231 중위순회

for tc in range(1,11):
    N = int(input())
    Tree = [] # idx별 자식 노드
    lst = [] # 노드 모음 1번 인덱스부터 노드의 원소가 들어간다.
    Tree.append([-1,-1])
    lst.append(0)

    dic = {}
    for i in range(N):
        InputLst = input().split()
        if len(InputLst) == 4:
            lst.append(InputLst[1]) # 노드 값 넣겠다.
            dic[InputLst[1]] = int(InputLst[0])
            Tree.append([int(InputLst[2]),int(InputLst[3])])
        elif len(InputLst) == 3:
            lst.append(InputLst[1])
            dic[InputLst[1]] = int(InputLst[0])
            Tree.append([int(InputLst[2]),-1])
        else: # len(InputLst) == 2:
            lst.append(InputLst[1])
            dic[InputLst[1]] = int(InputLst[0])
            Tree.append([-1,-1])

    def inorder(par):
        children1 ,children2 = Tree[dic[par]][0], Tree[dic[par]][1]
        if children1 != -1:
            inorder(lst[children1])
        print(par, end='')
        if children2 != -1:
            inorder(lst[children2])

    # print(dic)
    # print(lst)
    # print(Tree)

    print(f'#{tc}',end=' ')
    inorder(lst[1])
    print()








