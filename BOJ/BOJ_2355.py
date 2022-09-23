# BOJ_2355 math-sigma

# st,ed = map(int,input().split())
#
# print(((st+ed)/2)*(ed - st + 1))

total = 0
for i in range(st,ed+1):
    total += i

print(total)

