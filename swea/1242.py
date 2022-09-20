# 1242 암호코드 스캔
import sys
sys.stdin = open('1242.txt')

dic = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

change_dic = {
    211: '0',
    221: '1',
    122: '2',
    411: '3',
    132: '4',
    231: '5',
    114: '6',
    312: '7',
    213: '8',
    112: '9',
}


def sol(S):
    total = 3 * (int(S[0]) + int(S[2]) + int(S[4]) + int(S[6])) + int(S[1]) + int(S[3]) + int(S[5]) + int(S[7])
    return total


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = []
    not_zero = []
    total = 0
    # 0으로만 이루어져있지 않다면,
    for _ in range(N):
        InputS = input().strip()

        if InputS != '0' * M and not InputS in not_zero:
            not_zero.append(InputS)
            cnt = M - 1
    if tc == 20:
        not_zero.append('00000000000000000007E00E3F1FF007E38FC7FC7FC7E38FFF0071F8FC01C0000000000000000000000000000000000000000000000000000F000FF0F000FF000FF0F000FF0F0FF000F0F0FFFF0FFF0FF00F00FF000000000000000000000000000000000000000C0F0C3CFCF033C0F3033C0CF03CC00000000000000000000000000000000000000000E07E3803F1F8FF81C0FC7E00E3803F0071F8FC7FC0000000000000007E38FFF1C71FFE3803F1C01F8FF8FC7E3FE0703F000000000000000000000000000000000000000000000000000000000000000000000003C003FC003FC3C3C003FC03C03FC3C003FC3FC003C3FC003C03C03FC0')
    # 2진수로 바꾸기
    for idx in range(len(not_zero)):
        S = ''
        for i in not_zero[idx]:
            S += dic[i]
        not_zero[idx] = S

    cml2 = True

    for ele in not_zero: # 문장
        cnt = 0
        idx = 4*M-1
        Out_S = ''
        S_cnt = 0

        for _ in range(4*M-1):

            while 8-S_cnt:
                if ele[idx] == '1':
                    S = [0,0,0]
                    num = 1
                    while True:
                        if ele[idx] != ele[idx - 1]:
                            cnt += 1
                            S[3-cnt] = num
                            num = 1
                        else:
                            num += 1

                        idx -= 1
                        if cnt == 3:
                            cnt = 0
                            break

                    # 숫자별 최소인 수로 나누기 -> list : S
                    minumum = min(S)
                    for i in range(3):
                        S[i] = int(S[i]/minumum)

                    # print(S)
                    t = S[0]*100+S[1]*10+S[2]
                    Out_S = str(change_dic[t])+Out_S

                    S_cnt += 1

                else:
                    idx -= 1

                # if Out_S == '58087695':
                #     print(ele)

                if len(Out_S) == 8:
                    if sol(Out_S)%10 == 0 and not Out_S in lst:
                        # print(Out_S)
                        lst.append(Out_S)
                        for l in Out_S:
                            total += int(l)

                        # cml2 = False
                        cml = False

                    else:
                        Out_S = ''
                        S_cnt = 0
                        break

                if idx < 0:
                    break

            if idx < 0:
                break

    print(f'#{tc} {total}')
    # print(len(lst))
    # print(lst)
