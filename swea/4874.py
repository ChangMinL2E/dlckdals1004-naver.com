import sys
sys.stdin = open('4874.txt')

# 수정하세요.

T = int(input())

for tc in range(1, T + 1):
    stk = []
    N = list(input().split())
    test_st = []
    stk = []

    for n in N:
        if n in ['*', '-', '/', '+', '.']:
            test_st.append(n)
        else:
            stk.append(int(n))

    if len(test_st) != len(stk):
        out = f'#{tc} error'
    else:
        for i in range(len(test_st)):
            if test_st[i] == '*':
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1 * n2))
            elif n == '/':
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1 / n2))
            elif n == '+':
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1 + n2))
            elif n == '-':
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1 - n2))
            else:
                n1 = stk.pop()
                out = f'#{tc} {n1}'

    print(out)
