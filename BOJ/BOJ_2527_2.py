# BOJ_2527_2 사각형 순서를 거꾸로 생각해보자.
# d->c->b->a 로 가자.

for _ in range(4):

    a1, b1, a2, b2, c1, d1, c2, d2 = map(int, input().split())

    if a2 < c1 or a1 > c2 or b2 < d1 or b1 > d2: # 안겹치는거 빼고,
        print('d')

    # 여기서 부터는 무조건 겹침.
    elif (a1 == c2 and b1 == d2) or (a2 == c1 and b2 == d1):
        print('c')

    elif (a2 == c1 and b1 == d2) or (a1 == c2 and b2 == d1):
        print('c')

    elif b2 == d1 :
        if a1 == c2 or a2 == c1:
            print('c')
        # if not (a1 < c2 or c1 < a2):
        else:
            print('b')
    elif b1 == d2:
        if a1 == c2 or a2 == c1:
            print('c')
        # if not (a1 < c2 or c1 < a2):
        else:
            print('b')

    elif a2 == c1:
        if b1 == d2 or b2 == d1:
            print('c')
        # if not (d1 < b2 or b1 < d2):
        else:
            print('b')
    elif a1 == c2:
        if b1 == d2 or b2 == d1:
            print('c')
        # if not (d1 < b2 or b1 < d2):
        else:
            print('b')

    else:
        print('a')
