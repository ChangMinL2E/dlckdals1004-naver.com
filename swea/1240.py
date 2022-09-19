# swea.1240 단순 2진 암호코드

dic = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    Passwords = [input() for _ in range(N)]
    decoding = []
    cml = False

    for password in Passwords:
        if password != ['0'*M]:
            for idx in range(M-1,-1,-1):
                if password[idx] == '1':
                    S = password[idx-55:idx+1]
                    cml = True
                    break
            if cml:
                break
    # print(lst)
    for i in range(0,len(S),7):
        decoding.append(dic[S[i:i+7]])


    total = 0
    for idx in range(0,8,2):
        total += decoding[idx]*3+decoding[idx+1]

    if total % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(decoding)}')


