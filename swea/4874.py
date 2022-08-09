import sys
sys.stdin = open('4874.txt')

# 수정하세요.

T = int(input())

for tc in range(1, T + 1):
    stk = []
    N = list(input().split())
    stk = []

    for n in N:
        if n not in ['*', '-', '/', '+', '.']:
            stk.append(int(n))
        elif n == '*':
            if len(stk) <= 1:
                out = f'#{tc} error'
                break
            else:
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1 * n2))
        elif n == '/':
            if len(stk) <= 1:
                out = f'#{tc} error'
                break
            else:
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1 / n2))
        elif n == '+':
            if len(stk) <= 1:
                out = f'#{tc} error'
                break
            else:
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1 + n2))
        elif n == '-':
            if len(stk) <= 1:
                out = f'#{tc} error'
                break
            else:
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1 - n2))
        else:
            if len(stk) == 1:
                n1 = stk.pop()
                out = f'#{tc} {n1}'
            else:
                out = f'#{tc} error'

    print(out)
