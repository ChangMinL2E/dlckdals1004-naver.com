# 건물 조망 좋은 세대수 구하기

for tc in range(1,11):
    N = int(input())
    total = 0
    High = list(map(int,input().split()))

    for idx in range(len(High)):
        if (idx == 0) or (idx == 1) or (idx == len(High)-2) or (idx == len(High)-1):
            pass
        else:
            Highs = [High[idx+2-index] for index in range(5)] # High[idx-2],...,High[idx+2]
            Highs = sorted(Highs, reverse=True)
            if Highs[0] == High[idx]:
                total += Highs[0] - Highs[1]
            else:
                pass

    print(f'#{tc} {total}')


