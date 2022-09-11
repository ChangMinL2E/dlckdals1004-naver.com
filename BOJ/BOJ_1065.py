# BOJ_1065 함수 한수

def seq(n):
    if n<100:
        return n
    elif 100<=n<=999:
        total = 0
        for num in range(100,n+1):
            a,b,c = int(str(num)[0]), int(str(num)[1]), int(str(num)[2])
            if a - b == b - c:
                total += 1
        return 99+total
    else:
        return 144

print(seq(int(input())))

