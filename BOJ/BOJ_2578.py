# 2578 빙고

Bingo = []
for _ in range(5):
    Bingo.append(list(map(int, input().split())))  # 빙고판 제작

lst = []
for _ in range(5):
    inputS = input().split()
    for S in inputS:
        lst.append(int(S))

CheckCnt = 0
row = {}
col = {}
Cross1 = 0  # i,i
Cross2 = 0  # i,5-i
cnt = 0
for idx in range(5):
    row[idx] = 0
    col[idx] = 0

for ele in lst:
    cnt += 1
    for i in range(5):
        cml = True

        for j in range(5):
            if Bingo[i][j] == ele:
                row[i] += 1
                col[j] += 1
                if i == j:
                    Cross1 += 1
                if i + j == 4:
                    Cross2 += 1

                if row[i] == 5:
                    CheckCnt += 1
                if col[j] == 5:
                    CheckCnt += 1
                if Cross1 == 5:
                    CheckCnt += 1
                    Cross1 = 6
                if Cross2 == 5:
                    CheckCnt += 1
                    Cross2 = 6
                cml = False
                break

        if not cml:
            break

    if CheckCnt >= 3:
        print(cnt)
        break
