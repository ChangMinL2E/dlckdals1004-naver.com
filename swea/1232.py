# # 1232 트리 - 사칙연산

for tc in range(1,11):
    N = int(input())
    Tree = [0]
    for _ in range(N):
        Input_list = list(input().split())
        if len(Input_list) == 2:
            Tree.append(int(Input_list[1]))
        else:
            Tree.append(Input_list[1:])

    for idx in range(N,0,-1):
        if type(Tree[idx]) != int:
            Tree[idx][1], Tree[idx][2] = int(Tree[idx][1]) , int(Tree[idx][2])
            if Tree[idx][0] == '+':
                Tree[idx] = Tree[int(Tree[idx][1])]+ Tree[int(Tree[idx][2])]
            elif Tree[idx][0] == '-':
                Tree[idx] = Tree[int(Tree[idx][1])]- Tree[int(Tree[idx][2])]
            elif Tree[idx][0] == '*':
                Tree[idx] = Tree[int(Tree[idx][1])]* Tree[int(Tree[idx][2])]
            elif Tree[idx][0] == '/':
                Tree[idx] = Tree[int(Tree[idx][1])]/ Tree[int(Tree[idx][2])]

    print(f'#{tc} {int(Tree[1])}')

