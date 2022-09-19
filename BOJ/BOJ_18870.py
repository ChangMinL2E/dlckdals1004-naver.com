# BOJ_18870 좌표 압축
# for-for 를 쓰기보다는 for * 3 을 쓰는게 시간이 짧게 소요된다.

N = int(input())
lst = list(map(int,input().split()))
Sort_lst = sorted(list(set(lst)))
new_lst = []

dic = {}
for ls in lst:
    dic[ls] = 0

for i in range(len(Sort_lst)):
    dic[Sort_lst[i]] = i

for ls in lst:
    print(dic[ls], end=' ')

