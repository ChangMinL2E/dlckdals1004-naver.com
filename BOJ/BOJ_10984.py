# BOJ_10984 내 학점을 구해줘

for tc in range(1,int(input())+1):
    N = int(input())
    total = 0
    cnt = 0
    for _ in range(N):
        a, b = map(float,input().split())
        total += a*b
        cnt += a

    average = total / cnt

    print(round(cnt), round(average,1))

