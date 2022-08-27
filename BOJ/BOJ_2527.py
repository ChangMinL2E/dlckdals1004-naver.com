# BOJ_2527 직사각형

for _ in range(4):

    a1, b1, a2, b2, c1, d1, c2, d2 = map(int,input().split())

    out = 'd'

    if a1<c1<a2:
        if b1 < d1 < b2:
            out = 'a'
        elif d1 < b1:
            if b1 < d2:
                out = 'a'

    elif a1<c2<a2:
        if b1 < d2 < b2:
            out = 'a'
        elif b2 < d2:
            if d1 < b2:
                out = 'a'

    elif b2 == d1:
        if c1 < a2:
            out = 'b'
        elif c1 == a2:
            out = 'c'

    elif b1 == d2:
        if a1 < c2:
            out = 'b'
        elif a1 == c2:
            out = 'c'

    elif a2 == c1:
        if d1<b2:
            out = 'b'
        elif d1 == b2:
            out = 'c'

    elif a1 == a2:
        if b1<b2:
            out = 'b'
        elif b1 == d2:
            out = 'c'

    print(out)