for tc in range(int(input())):
    max = 0
    min = 1000000
    N, M = map(int ,input().split(" "))
    result = 0

    numList = list(map(int , input().split(" ")))

    
    
    idx = 0
    for num in numList:
        if sum(numList[idx:idx+M]) < min:
            min = sum(numList[idx:idx+M]) 
        else:
            if sum(numList[idx:idx+M]) > max:
                max = sum(numList[idx:idx+M])
            else:
                continue
        idx+=1
        
    
    
    result = max - min

    print(f'# {tc+1} {result}')