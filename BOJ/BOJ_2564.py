# BOJ_2564 경비원

x, y = map(int, input().split())
N = int(input())
lst = [0] * (x + y) * 2

for num in range(1, N + 1):
    shop = list(map(int, input().split()))  # 위치 좌표 (동, 4) 처럼
    if shop[0] == 1:
        lst[shop[1] - 1] += 1
    elif shop[0] == 2:
        lst[2 * x + y - shop[1] - 1] += 1
    elif shop[0] == 3:
        lst[2 * (x + y) - shop[1] - 1] += 1
    else:
        lst[x + shop[1] - 1] += 1

shot = list(map(int, input().split()))
if shot[0] == 1:
    shot = shot[1] - 1
elif shot[0] == 2:
    shot = 2 * x + y - shot[1] - 1
elif shot[0] == 3:
    shot = 2 * (x + y) - shot[1] - 1
else:
    shot = x + shot[1] - 1

total = 0

for idx in range(len(lst)):
    if lst[idx] != 0:
        gap = abs(shot - idx)
        total += lst[idx]*min(gap, 2*(x+y)-gap)

print(total)