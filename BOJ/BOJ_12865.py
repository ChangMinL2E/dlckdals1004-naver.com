# BOJ_12865 평범한 배낭
# 냅색

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
d = [0] * (K + 1)
for _ in range(N):
    w, v = map(int, input().split())
    # 가방 안에 중복해서 넣으면 안되므로 뒤에서부터 넣음
    for i in range(K, w - 1, -1):
        d[i] = max(d[i], d[i - w] + v) # 기존 최대랑, 고른 가중치랑 같이 들수있는 가중치의 최대치의 합이랑 비교
print(max(d))
