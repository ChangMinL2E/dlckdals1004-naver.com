# BOJ_1991 트리 순회

N = int(input())

lst = []
Tree = []
dic = {}  # 알파벳 노드 넘버

for i in range(N):
    a, b, c = map(str, input().split())
    lst.append(a)
    Tree.append([b, c])
    dic[a] = i


def pre(par):  # global 변수처럼 전위순회 사용
    parent = par
    children1, children2 = Tree[dic[parent]][0], Tree[dic[parent]][1]
    print(parent, end='')
    if children1 != '.':
        pre(Tree[dic[children1]], children1)  # 좌측
    if children2 != '.':
        pre(Tree[dic[children2]], children2)  # 우측


def inorder(par):
    parent = par
    children1, children2 = Tree[dic[parent]][0], Tree[dic[parent]][1]
    if children1 != '.':
        inorder(Tree[dic[children1]], children1)  # 좌측
    print(parent, end='')
    if children2 != '.':
        inorder(Tree[dic[children2]], children2)  # 우측


def postorder(par):
    parent = par
    children1, children2 = Tree[dic[parent]][0], Tree[dic[parent]][1]
    if children1 != '.':
        postorder(Tree[dic[children1]], children1)  # 좌측
    if children2 != '.':
        postorder(Tree[dic[children2]], children2)  # 우측
    print(parent, end='')


pre(lst[0])
print()
inorder(lst[0])
print()
postorder(lst[0])
