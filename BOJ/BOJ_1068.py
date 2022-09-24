# BOJ_1068 트리 / 트리 생성 후, 노드 하나 제거후, 리프노드 개수 구하기.
from collections import deque

N = int(input())

Tree = [[-1,-1] for _ in range(N)]
leafs = [True]*N

# 입력받은 부모 노드들
lst = list(map(int,input().split()))
leaf_lst = [x for x in range(N)]

dic = {}

for idx in range(len(lst)):
    if lst[idx] != -1:
        if Tree[lst[idx]][0] == -1: # Tree 부모노드의 앞자리가 비었으면,
            Tree[lst[idx]][0] = idx
        else:
            Tree[lst[idx]][1] = idx
        dic[idx] = lst[idx]
    else: # -1 루트면,
        dic[idx] = -1

        leafs[lst[idx]] = False # 부모노드로 선정된 노드들은 리프가 아니다.

delete_node = int(input())

Queue = deque()
Queue.append(delete_node)
while Queue:
    node = Queue.popleft()
    leafs[node] = False
    leaf_lst.remove(node)
    if Tree[node] != -1:
        for i in range(len(Tree[dic[node]])):
            if Tree[dic[node]][i] == node:
                Tree[dic[node]][i] = -1
    else: # 노드가 루트면,
        leafs = [False]*N
        leaf_lst = []
        Queue = []

    for ele in Tree[node]:
        if ele != -1:
            Queue.append(ele)


for ele in leaf_lst:
    if Tree[ele] == [-1,-1]:
        leafs[ele] = True
    else:
        leafs[ele] = False

# print(leaf_lst)
# print(Tree)
# print(leafs)

print(leafs.count(True))



