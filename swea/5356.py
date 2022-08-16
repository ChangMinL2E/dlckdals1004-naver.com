# 5356. 의석이의 세로로 말해요.

for tc in range(1, int(input()) + 1):
    lst = []
    for _ in range(5):
        N = list(input()) # 입력받은 문자열 배열 5 X 자연수
        lst.append(N)

    max_length = 0
    for num in lst:
        if max_length < len(num): # 가장 큰 열의 길이
            max_length = len(num)

    N_lst = []
    for i in range(5):
        N_lst.append([]) # 5 X max_length 배열 만들기.
        for _ in range(max_length):
            N_lst[i].append('')

    for k in range(5):  # 존재하는 원소들은 대입, 없는 자리에는 빈 문자열.
        for l in range(len(lst[k])):
            N_lst[k][l] = lst[k][l]

    print_lst = []

    for j in range(max_length):
        for i in range(5):
            print_lst.append(N_lst[i][j])

    print_st = ''.join(print_lst)

    print(f'#{tc} {print_st}')
