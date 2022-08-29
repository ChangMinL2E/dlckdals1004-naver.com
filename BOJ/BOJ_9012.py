# BOJ_9012 괄호

for _ in range(int(input())):
    VPS = list(input())
    Stk = []
    out = "YES"

    for vps in VPS:
        if vps == '(':
            Stk.append(vps)
        elif vps == ')':
            if len(Stk) == 0:
                out = "NO"
                break
            elif Stk[-1] == '(':
                Stk.pop()

    if len(Stk) != 0:
        out = 'NO'

    print(out)