# BOJ_14696.py
# 30점

N = int(input())

for _ in range(N):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if A.count(4) > B.count(4):
        print('A')
    elif A.count(4) < B.count(4):
        print('B')
    else:
        if A.count(3) > B.count(3):
            print('A')
        elif A.count(3) < B.count(3):
            print('B')
        else:
            if A.count(2) > B.count(2):
                print('A')
            elif A.count(2) < B.count(2):
                print('B')
            else:
                if A.count(1) > B.count(1):
                    print('A')
                elif A.count(1) < B.count(1):
                    print('B')
                else:
                    print('D')