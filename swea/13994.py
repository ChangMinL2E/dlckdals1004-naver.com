# 새로운 버스 노선

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst1 = []
    lst2 = []
    lst3 = []

    for _ in range(N):
        C, A, B = map(int, input().split())
        if C == 1:
            for num1 in range(A, B + 1):
                lst1.append(num1)
        elif C == 2:
            if A % 2 == 0:
                for num2 in range(A, B, 2):
                    lst2.append(num2)
                if B not in lst2:
                    lst2.append(B)
            else:
                for num2 in range(A, B, 2):
                    lst2.append(num2)
                if B not in lst2:
                    lst2.append(B)
        else:
            if A % 2 == 0:
                for num3 in range(A, B):
                    if num3%4 == 0:
                        lst3.append(num3)
                if B not in lst3:
                    lst3.append(B)
            else:
                for num3 in range(A, B):
                    if num3%10:
                        lst3.append(num3)
                if B not in lst3:
                    lst3.append(B)

    total = []
    for n1 in lst1:
        total.append(n1)
    for n1 in lst2:
        total.append(n1)
    for n1 in lst3:
        total.append(n1)
    total = list(set(total))

    max_num = 1

    for num in total:
        if (num in lst1) and (num in lst2) and (num in lst3):
            max_num = 3
            break
        elif (num in lst1) and (num in lst2):
            max_num = 2

        elif (num in lst2) and (num in lst3):
            max_num = 2

        elif (num in lst1) and(num in lst3):
            max_num = 2

    print(f'#{tc} {max_num}')