# 06 그래프 - 그룹나누기
# 10개중 9개 정답

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    papers = list(map(int,input().split()))

    group_lst = []
    group_cnt = 0
    visit_members = set()

    for i in range(M):
        a,b = papers[2*i], papers[2*i+1]
        idx1, idx2 = -1,-1
        button = 0

        for num in range(len(group_lst)):
            if a in group_lst[num]:
                idx1 = num
                button += 1
            if b in group_lst[num]:
                idx2 = num
                button += 1

            if button == 2:
                break
        if button == 2:
            group_cnt -= 1
        elif button == 0:
            group_lst.append([a,b])
            group_cnt += 1
        else: # button == 1:
            if idx1 != -1:
                group_lst[idx1].append(b)
            else: # idx2 != -1:
                group_lst[idx2].append(a)

        visit_members = visit_members | set([a,b])

    # print(visit_members)
    # print(group_lst)
    # print(group_cnt)
    print(f'#{tc} {group_cnt+N-len(visit_members)}')
