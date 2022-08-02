# 특별한 정렬


T = int(input())
# T = 1

for tc in range(1,T+1):
    N = int(input())
    org = list(map(int,input().split()))
    lst1 = sorted(org,reverse=True)
    lst2 = sorted(org)
    new_lst = []
    for i in range(5):
        new_lst.append(lst1[i])
        new_lst.append(lst2[i])
    
    new_st = ''
    for j in new_lst:
        new_st += str(j)+' '

    print(f'#{tc} {new_st}')

