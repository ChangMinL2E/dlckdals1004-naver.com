# 주식가격

'''
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''

# from collections import deque
def solution(prices):
    answer = []
    lst = [0]*len(prices)
    
    queue = [0]
    idx = 1
    while True:
        if idx == len(prices)-1:
            for q in queue:
                if q != len(prices)-1:
                    lst[q] = len(prices)-1-q
            break
        
        for i in range(len(queue)-1,-1,-1):
            if prices[queue[i]] > prices[idx]:
                lst[queue[i]] = idx-queue[i]
                queue.pop(i)
        queue.append(idx)
        idx += 1
    
    return lst