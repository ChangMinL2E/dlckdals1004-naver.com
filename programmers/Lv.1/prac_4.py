# 체육복

'''
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''

def solution(n, lost, reserve):

    Gyo = set(lost)&set(reserve)
    lost, reserve = sorted(list(set(lost)-Gyo)),sorted(list(set(reserve)-Gyo))
    
    for num in lost[::-1]:
        if num+1 in reserve:
            lost.remove(num)
            reserve.remove(num+1)
        elif num-1 in reserve:
            lost.remove(num)
            reserve.remove(num-1)
        

    return n-len(lost)