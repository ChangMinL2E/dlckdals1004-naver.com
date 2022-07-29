# 13547 팔씨름 대회

T = int(input())
# T = 1

for tc in range(T):
    S = input()
    if 1<=len(S)<=15:
        if S.count('x')<8:
            print(f'#{tc+1} YES')
        else:
            print(f'#{tc+1} NO')
    else:
        print(f'#{tc+1} NO')
