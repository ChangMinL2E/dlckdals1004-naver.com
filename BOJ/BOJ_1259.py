# BOJ_1259 팰린드롬수

cml = True

while cml:
    inputS = input()
    if inputS == '0':
        cml = False
    else:
        if inputS == inputS[::-1]:
            print('yes')
        else:
            print('no')