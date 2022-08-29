# BOJ_11721 열 개씩 끊어 출력하기

inputS = input()

cml = True
while cml:
    if len(inputS) >= 10:
        print(inputS[:10])
        inputS = inputS[10:]
    else:
        print(inputS)
        cml = False


