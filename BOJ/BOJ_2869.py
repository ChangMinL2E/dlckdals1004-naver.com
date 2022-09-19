# BOJ_2869 달팽이는 올라가고 싶다.

A, B, V = map(int,input().split())

G = (V-A)//(A-B)
cnt = G
total = G*(A-B)

while True:
    cnt += 1
    total += A
    if total >= V:
        break
    else:
        total -= B

print(cnt)