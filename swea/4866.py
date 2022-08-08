# 괄호 검사
# Runtime error

T = int(input())
for tc in range(1,T+1):
    N = input()
    A = ['{','[','(']
    B = ['}',']',')']
    test = []
    for st in N:
        if st in A:
            test.append(st)
        elif st in B:
            for i in range(3):
                if (st == B[i]):
                    if (test[-1] == A[i]):
                        test.pop()

    if test == []:
        out = f'#{tc} 1' 
    else:
        out = f'#{tc} 0'
    print(out)
                    



