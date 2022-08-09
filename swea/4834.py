# T = int(input())
# # T = 1

# for tc in range(1,T+1):
#     N = int(input())
#     N2 = input()
#     lst = []
#     for i in range(N):
#         lst.append(int(N2[i]))
    


#     high = 0
#     for j in range(10):
#         if lst.count(j) > lst.count(high):
#             high = j
#         elif lst.count(j) == lst.count(high):
#             if j > high:
#                 high = j
    
#     print(f'#{tc} {high} {lst.count(high)}')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    N2 = input()
    lst = []
    for n2 in N2:
        lst.append(int(n2))
    
    Cnt = [0]*10 # 각 숫자별 원소 갯수 리스트
    for ls in lst:
        Cnt[ls] += 1
    
    high = 0
    for cn in Cnt: # 가장 많은 개수 뽑기.
        if cn > high:
            high = cn
    
    high_ele = 0
    for i in range(len(Cnt)): # 가장 많은 원소 뽑기.
        if Cnt[i] == high:
            if i > high_ele:
                high_ele = i
    
    print(f'#{tc} {high_ele} {high}')




