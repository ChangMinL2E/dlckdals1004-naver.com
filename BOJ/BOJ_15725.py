# BOJ_15725 다항함수의 미분

InputS = input()
for i in range(1,len(InputS)):
    if InputS[i] == 'x':
        if i == 0:
            print(1)
        elif i == 1:
            if InputS[0] == '-':
                print(-1)

        elif InputS[i-2] == '-':
            print(InputS[i-2:i])
        else:
            print(InputS[i-1])