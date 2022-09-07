# BOJ_10828 스택
# Runtime_error

STK = []

for _ in range(int(input())):
    InputS = input()
    if InputS == "pop":
        if len(STK) == 0:
            print(-1)
        else:
            print(STK.pop())
    elif InputS == 'top':
        if len(STK) == 0:
            print(-1)
        else:
            print(STK[-1])
    elif InputS == "empty":
        if len(STK) == 0:
            print(1)
        else:
            print(0)
    elif InputS == 'size':
        print(len(STK))
    else:
        InputS = InputS.split()
        STK.append(int(InputS[-1]))


