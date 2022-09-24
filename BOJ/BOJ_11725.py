# BOJ_11725 트리 / 부모 찾기
# 왜 틀렸는지 모르겠네.

import sys

N = int(sys.stdin.readline().strip())
# 트리 만들자.
tree = [[0,0] for _ in range(N+1)]

# 입력이 부모 - 자식 이 아니라 랜덤이다.

tree_dic = {1:0} # 순서를 정해주겠다.
for i in range(2,N+1):
    tree_dic[i] = -1

for _ in range(N-1):
    a, b = map(int,sys.stdin.readline().split())
    if a == 1: # a가 루트이면,
        parent, child = a,b
        tree_dic[b] = 1
    elif b == 1:
        parent, child = b,a
        tree_dic[a] = 1 # 레벨을 정해주는것이다.
    else:
        # 처음 나오는 정점이면, 레벨을 정해주겠다.
        if tree_dic[a] == -1:
            parent, child = b,a
            tree_dic[a] = tree_dic[b]+1
        elif tree_dic[b] == -1:
            parent, child = a,b
            tree_dic[b] = tree_dic[a] + 1
        # 이미 둘다 나온경우, 레벨을 비교해서 부모를 정하겠다.
        else:
            if tree_dic[a] < tree_dic[b]:
                parent, child = a,b
            elif tree_dic[b] < tree_dic[a]:
                parent, child = b,a
    # 트리 만들겠다.
    if tree[parent][0] == 0:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

parents_list = [-1,-1] # 부모 명단 0과 1은 부모명단에 -1 넣어뒀다.
parents_list.extend([0]*(N-1))

for idx in range(len(tree)):
    for i in range(2):
        if tree[idx][i] != 0:
            parents_list[tree[idx][i]] = idx


for i in range(2,N+1):
    print(parents_list[i])







