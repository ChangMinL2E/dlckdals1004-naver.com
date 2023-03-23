# 타겟 넘버

'''
numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
'''


answer = 0

def solution(numbers, target):
    global answer
    Permutation(len(numbers),0,0,numbers, target)

    return answer

def Permutation(N,k,total,lst, target):
    global answer
    
    if N == k:
        if total == target:
            answer += 1
            return
        else:
            return 0
    
    Permutation(N,k+1,total+lst[k],lst,target)
    Permutation(N,k+1,total-lst[k],lst,target)