T = int(input())
# T = 1

for tc in range(1,T+1):
    N = int(input())
    N2 = input()
    lst = []
    for i in range(N):
        lst.append(int(N2[i]))
    
    high = 0
    for j in range(10):
        if lst.count(j) > lst.count(high):
            high = j
        elif lst.count(j) == lst.count(high):
            if j > high:
                high = j
    
    print(f'#{tc} {high} {lst.count(high)}')





