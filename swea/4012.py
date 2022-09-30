# 4012 요리사

def permutation(lst1, lst2,k):
    global minimum

    if k == N:
        total1 = 0
        total2 = 0
        for i in range(int(N/2)):
            for j in range(int(N/2)):
                total1 += Lst[lst1[i]][lst1[j]]
                total2 += Lst[lst2[i]][lst2[j]]
        if abs(total1-total2) < minimum:
            minimum = abs(total1-total2)

        return

    if len(lst1)!= N/2 and len(lst2)!= N/2:
        lst1.append(k)
        permutation(lst1,lst2,k+1)
        lst1.pop()
        lst2.append(k)
        permutation(lst1,lst2,k+1)
        lst2.pop()

    elif len(lst1) == N/2 and len(lst2) != N/2:
        lst2.append(k)
        permutation(lst1, lst2, k + 1)
        lst2.pop()

    elif len(lst1) != N/2 and len(lst2) == N/2:
        lst1.append(k)
        permutation(lst1, lst2, k + 1)
        lst1.pop()



for tc in range(1,int(input())+1):
    minimum = 1e10
    N = int(input())
    Lst = [list(map(int,input().split())) for _ in range(N)]
    permutation([],[],0)

    print(f'#{tc} {minimum}')




