for tc in range(1, int(input())+1):
    N = input()
    stk = []
    opn = ['{','(']
    out = f'#{tc} 1'

    for st in N:
        if st in opn:
            stk.append(st)
        elif st == '}':
            if len(stk) > 0 and stk[-1] == '{' :
                stk.pop()
            else:
                out = f'#{tc} 0'
                break
        elif st == ')':
            if len(stk) > 0 and stk[-1] == '(':
                stk.pop()
            else:
                out = f'#{tc} 0'
                break

    if len(stk) == 0:
        print(out)
    else:
        out = f'#{tc} 0'
        print(out)
