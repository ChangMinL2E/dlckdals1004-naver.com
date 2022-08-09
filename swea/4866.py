# 괄호 검사
# Runtime error

T = int(input())
for tc in range(1, T + 1):
    N = input()
    A = ['{', '(']
    B = ['}', ')']
    test = []
    num = 0
    for st in N:
        if st in A:
            test.append(st)
            num += 1
        elif st in B:
            if len(test) == 0:
                out = f'#{tc} 0'
                break
            elif B.index(st) == A.index(test[-1]):
                test.pop()
                num -= 1
            else:
                out = f'#{tc} 0'
                break

    if num == 0:
        out = f'#{tc} 1'
    else:
        out = f'#{tc} 0'
    print(out)
