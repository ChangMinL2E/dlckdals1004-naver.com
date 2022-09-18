# swea 4615 오델로
# B: 흑돌, W: 백돌

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    Black = [(N//2,N//2-1),(N//2-1,N//2)]
    White = [(N//2,N//2),(N//2-1,N//2-1)]

    for _ in range(M):
        a,b,color = map(int,input().split())
        row, col = b-1, a-1

        lst = []
        # 흑돌

        if color == 1:
            # 가로 - 우
            row_lst = []
            for i in range(1,N):
                if 0<= col+i<= N-1:
                    if (row,col+i) in White:
                        row_lst.append((row,col+i))
                    elif (row,col+i) in Black:
                        lst.extend(row_lst)
                        row_lst.clear()
                        break
                    else:
                        row_lst.clear()
                        break
                else:
                    row_lst.clear()
                    break

            # 가로 - 좌
            for i in range(1,N):
                if 0 <= col - i <= N - 1:
                    if (row, col - i) in White:
                        row_lst.append((row, col - i))
                    elif (row, col - i) in Black:
                        lst.extend(row_lst)
                        row_lst.clear()
                        break
                    else:
                        row_lst.clear()
                        break
                else:
                    row_lst.clear()
                    break

            col_lst = []
            # 세로 - 상
            for j in range(1,N):
                if 0<= row-j<= N-1:
                    if (row-j, col) in White:
                        col_lst.append((row-j, col))
                    elif (row-j, col) in Black:
                        lst.extend(col_lst)
                        col_lst.clear()
                        break
                    else:
                        col_lst.clear()
                        break
                else:
                    col_lst.clear()
                    break

            # 세로 - 하
            for j in range(1,N):
                if 0<= row+j<= N-1:
                    if (row+j, col) in White:
                        col_lst.append((row+j, col))
                    elif (row + j, col) in Black:
                        lst.extend(col_lst)
                        col_lst.clear()
                        break
                    else:
                        col_lst.clear()
                        break
                else:
                    col_lst.clear()
                    break

            dia_lst = []
            # 대각선 우 상향
            for k in range(1,N):
                if 0<= col+k<= N-1 and 0<= row-k<= N-1:
                    if (row-k, col+k) in White:
                        dia_lst.append((row-k, col+k))
                    elif (row - k, col + k) in Black:
                        lst.extend(dia_lst)
                        dia_lst.clear()
                        break
                    else:
                        dia_lst.clear()
                        break
                else:
                    dia_lst.clear()
                    break

            # 대각선 좌 상향
            for k in range(1,N):
                if 0 <= col - k <= N - 1 and 0 <= row - k <= N - 1:
                    if (row - k, col - k) in White:
                        dia_lst.append((row - k, col - k))
                    elif (row - k, col - k) in Black:
                        lst.extend(dia_lst)
                        dia_lst.clear()
                        break
                    else:
                        dia_lst.clear()
                        break
                else:
                    dia_lst.clear()
                    break

            # 대각선 좌 하향
            for k in range(1,N):
                if 0 <= col - k <= N - 1 and 0 <= row + k <= N - 1:
                    if (row + k, col - k) in White:
                        dia_lst.append((row + k, col - k))
                    elif (row + k, col - k) in Black:
                        lst.extend(dia_lst)
                        dia_lst.clear()
                        break
                    else:
                        dia_lst.clear()
                        break
                else:
                    dia_lst.clear()
                    break

            # 대각선 우 하향
            for k in range(1,N):
                if 0 <= col + k <= N - 1 and 0 <= row + k <= N - 1:
                    if (row + k, col + k) in White:
                        dia_lst.append((row + k, col + k))
                    elif (row + k, col + k) in Black:
                        lst.extend(dia_lst)
                        dia_lst.clear()
                        break
                    else:
                        dia_lst.clear()
                        break
                else:
                    dia_lst.clear()
                    break

            for ls in lst:
                White.remove(ls)

            Black.extend(lst)
            Black.append((row,col))

        if color == 2:
            # 가로 - 우
            row_lst = []
            for i in range(1,N):
                if 0 <= col + i <= N - 1:
                    if (row, col + i) in Black:
                        row_lst.append((row, col + i))
                    elif (row, col + i) in White:
                        lst.extend(row_lst)
                        row_lst.clear()
                        break
                    else:
                        row_lst.clear()
                        break
                else:
                    row_lst.clear()
                    break

            # 가로 - 좌
            for i in range(1,N):
                if 0 <= col - i <= N - 1:
                    if (row, col - i) in Black:
                        row_lst.append((row, col - i))
                    elif (row, col - i) in White:
                        lst.extend(row_lst)
                        row_lst.clear()
                        break
                    else:
                        row_lst.clear()
                        break
                else:
                    row_lst.clear()
                    break

            col_lst = []
            # 세로 - 상
            for j in range(1,N):
                if 0 <= row - j <= N - 1:
                    if (row - j, col) in Black:
                        col_lst.append((row - j, col))
                    elif (row - j, col) in White:
                        lst.extend(col_lst)
                        col_lst.clear()
                        break
                    else:
                        col_lst.clear()
                        break
                else:
                    col_lst.clear()
                    break

            # 세로 - 하
            for j in range(1,N):
                if 0 <= row + j <= N - 1:
                    if (row + j, col) in Black:
                        col_lst.append((row + j, col))
                    elif (row + j, col) in White:
                        lst.extend(col_lst)
                        col_lst.clear()
                        break
                    else:
                        col_lst.clear()
                        break
                else:
                    col_lst.clear()
                    break

            dia_lst = []
            # 대각선 우 상향
            for k in range(1,N):
                if 0 <= col + k <= N - 1 and 0 <= row - k <= N - 1:
                    if (row - k, col + k) in Black:
                        dia_lst.append((row - k, col + k))
                    elif (row - k, col + k) in White:
                        lst.extend(dia_lst)
                        dia_lst.clear()
                        break
                    else:
                        dia_lst.clear()
                        break
                else:
                    dia_lst.clear()
                    break

            # 대각선 좌 상향
            for k in range(1,N):
                if 0 <= col - k <= N - 1 and 0 <= row - k <= N - 1:
                    if (row - k, col - k) in Black:
                        dia_lst.append((row - k, col - k))
                    elif (row - k, col - k) in White:
                        lst.extend(dia_lst)
                        dia_lst.clear()
                        break
                    else:
                        dia_lst.clear()
                        break
                else:
                    dia_lst.clear()
                    break

            # 대각선 좌 하향
            for k in range(1,N):
                if 0 <= col - k <= N - 1 and 0 <= row + k <= N - 1:
                    if (row + k, col - k) in Black:
                        dia_lst.append((row + k, col - k))
                    elif (row + k, col - k) in White:
                        lst.extend(dia_lst)
                        dia_lst.clear()
                        break
                    else:
                        dia_lst.clear()
                        break
                else:
                    dia_lst.clear()
                    break

            # 대각선 우 하향
            for k in range(1,N):
                if 0 <= col + k <= N - 1 and 0 <= row + k <= N - 1:
                    if (row + k, col + k) in Black:
                        dia_lst.append((row + k, col + k))
                    elif (row + k, col + k) in White:
                        lst.extend(dia_lst)
                        dia_lst.clear()
                        break
                    else:
                        dia_lst.clear()
                        break
                else:
                    dia_lst.clear()
                    break

            for ls in lst:
                Black.remove(ls)

            White.extend(lst)
            White.append((row,col))

    print(f'#{tc} {len(Black)} {len(White)}')





