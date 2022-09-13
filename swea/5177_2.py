# 5177. 이진 최소 힙 다시 풀기

def min_heap(tree,node):
    global cnt
    idx = cnt
    cnt += 1

    tree[idx] = node
    while idx-1:
        if tree[idx] <= tree[idx//2]:
            tree[idx], tree[idx//2] = tree[idx//2],tree[idx]
            idx //= 2
        else:
            return

for tc in range(1,int(input())+1):
    N = int(input())
    Tree = [0]*501
    cnt = 1

    lst = list(map(int,input().split()))
    for ls in lst:
        min_heap(Tree,ls)

    total = 0
    while N-1:
        total += Tree[N//2]
        N //= 2

    print(f'#{tc} {total}')

