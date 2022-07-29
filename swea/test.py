# T = int(input())
T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n, m = map(int,input().split())
    if 5>n>15:
        n= int(input())
    if 2>m>n:
        m= int(input())

    fliesLst = [[0 for col in range(n)] for row in range(n)]
    flapper= [[0 for col in range(m)] for row in range(m)]
    max = 0

    for k in range(n):
        fliesLst.append(list(map(int, input().split())))

    for i in range(n-m+1):
        for j in range(n-m+1):#0~n-m까지 파리
            flapperSum=0
            for fi in range(m):
                for fj in range(m):#mxm 파리채
                    flapper.append(fliesLst[i+fi][j+fj])
                flapperSum=sum(flapper)
            if flapperSum>max:
                max= flapperSum

    print(f'#{test_case} {max}')