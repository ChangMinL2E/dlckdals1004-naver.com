# 1265. 달란트2

for tc in range(1,int(input())+1):
    total, cnt = map(int,input().split())
    out = 0
    if total % cnt == 0:
        out = (total//cnt)**cnt
    else:
        out = (total//cnt)**(cnt-total%cnt)*(total//cnt+1)**(total%cnt)

    print(f'#{tc} {out}')