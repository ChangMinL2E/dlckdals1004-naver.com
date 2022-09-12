# 03_Greedy Algorithm Baby-Gin
# Count_list 를 사용하자!
# 불공평한 게임임을 확인하라.

def Baby_Gin(lst):
    Count_list = [0]*10
    for ls in lst:
        Count_list[ls] += 1

    for idx in range(len(Count_list)):
        if Count_list[idx] == 3:
            return 1
        elif idx<=7 and (Count_list[idx] > 0 and Count_list[idx+1] > 0 and Count_list[idx+2] > 0):
            return 1

    return 0


for tc in range(1,int(input())+1):
    player1 = []
    player2 = []
    cards = list(map(int,input().split()))

    result = 0
    for i in range(0,12):
        # 불공평한 게임. 한장씩 동시에 나눠주는게 아니라 한장씩 조건에 맞게 주고, 비교한다.
        if not i % 2:
            player1.append(cards[i])
        else:
            player2.append(cards[i])
        if len(player1) >= 3:
            p1_r = Baby_Gin(player1)
            p2_r = Baby_Gin(player2)
            if p1_r and not p2_r: # 1번 선수만 이룰 시
                result = 1
                break
            elif not p1_r and p2_r: # 2번 선수만 이룰 시
                result = 2
                break
            elif p1_r and p2_r: # 둘 다 동시에 이룰 시
                break

    print(f'#{tc} {result}')


