# BOJ_2263 트리의 순회
# 실패 완전 이진트리가 아닌가보다.

N = int(input())

idx = 1
inorder_lst = [0]*(N+1)
inorder_Tree = list(map(int,input().split()))
input() # 후위 날리고
def inorder(i):
    global idx

    if i<N+1:
        inorder(2*i)
        inorder_lst[idx] = i
        idx += 1
        inorder(2*i+1)

inorder(1)
# print(inorder_lst)

Tree = [0]*(N+1)

for i in range(N+1):
    Tree[inorder_lst[i]] = inorder_Tree[i-1]

Tree[0] = 0
# print(Tree)

def preorder(i):
    if i < N+1:
        print(Tree[i], end=' ')
        preorder(i*2)
        preorder(i*2+1)

preorder(1)







