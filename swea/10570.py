# d3 10570 제곱 팰린드롬 수

# T = 1
T = int(input())

for tc in range(1,T+1):
    a,b = map(int,input().split())

    total = 0
    for num in range(a,b+1):
        if str(num) == str(num)[::-1]:
            num2 = num**0.5
            # print(num2)
            if num2%1 == 0.0:
                if str(int(num2)) == str(int(num2))[::-1]:
                    total += 1

    print(f'#{tc} {total}')        