# 다음에 올 숫자

'''
common	result
[1, 2, 3, 4]	5
[2, 4, 8]	16
'''

def solution(common):
    
    a = common[1]-common[0]
    b = common[2]-common[1]
    answer = 0
    # 등차수열이면,
    if a == b:
        answer = common[-1] + a
    else: # 등비수열이면,
        answer = common[-1]*(common[1]/common[0])
    return answer