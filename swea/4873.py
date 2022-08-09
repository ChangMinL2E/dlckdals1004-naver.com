# def delete(A):
#     isFind = False
#     # A1 = ''
#     for i in range(len(A)-1):
#         if A[i] == A[i+1]:
#             A1 = A[:i]+A[i+2:]
#             isFind = True
    
#     if not isFind:
#         return len(A1)
#     else:
#         return delete(A1)

def delete_len(A):
    lst = []
    A_lst = [a for a in A]

    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            if i not in lst:
                lst.append(i)
                lst.append(i+1)
    
    if len(lst) == 0:
        A2 = '0'
    else:
        for j in range(len(lst),0,-1):
            del A_lst[j]
        A2 = ''.join(A_lst)
    
    if A2 == '0':
        return len(A)
    else:
        return delete_len(A2)

T = int(input())
for tc in range(1,T+1):
    N = input()
    
    print(f'#{tc} {delete_len(N)}')


def delete(A):
    cml = True

    while cml:
        lst = []
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                if i not in lst:
                    lst.append(i)
                    lst.append(i+1)
    
        if len(lst) == 0:
            A2 = '0'
        else:
            for j in range(len(lst),0,-1):
                del A_lst[j]
            A2 = ''.join(A_lst)