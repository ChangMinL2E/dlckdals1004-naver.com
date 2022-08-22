# 중위, 후위 표기법

def behind(msg):
    stk = []
    sol = ''
    nonum = '(+-*/)'
    cnt = 1
    for ms in msg:
        if ms not in nonum: # 숫자면 그냥 적고,
            sol += ms
        elif ms in nonum[0]: # 여는 괄호 바로 넣고.
            stk.append(ms)

        elif ms in nonum[1:3]: # +,-
            cml = True
            while cml:
                if len(stk) == 0:
                    stk.append(ms)
                    cml = False
                elif stk[-1] in nonum[1:]:
                    sol += stk.pop()
                else:
                    stk.append(ms)
                    cml = False

        elif ms in nonum[3:5]: # *,/
            cml = True
            while cml:
                if len(stk) == 0:
                    stk.append(ms)
                    cml = False
                elif stk[-1] in nonum[3:5]:
                    sol += stk.pop()
                else:
                    stk.append(ms)
                    cml = False

        else: # )
            cml = True
            while cml:
                if stk[-1] == '(':
                    stk.pop()
                else:
                    cml = False

        if cnt == len(msg):
                cml = True
                while cml:
                    if len(stk) != 0:
                        sol += stk.pop()
                    else:
                        cml = False
        cnt += 1
    return sol

def bhmd(msg):
    stk = []
    nonum = '+-*/'

    for ms in msg:
        if ms not in nonum:
            stk.append(ms)
        else:
            b = int(stk.pop())
            a = int(stk.pop())
            if ms == '+':
                stk.append(str(a+b))
            elif ms == '-':
                stk.append(str(a-b))
            elif ms == '*':
                stk.append(str(a*b))
            elif ms == '/':
                stk.append(str(a/b))

    sol = stk.pop()
    return sol

for tc in range(1,11):
    input()
    N = input()

    print(f'#{tc} {bhmd(behind(N))}')

