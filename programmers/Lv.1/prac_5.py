# 정수 제곱근 판별

'''
n	return
121	144
3	-1
'''

def solution(n):
    answer = 0
    
    sqrt_n = n**(1/2)
    if abs(sqrt_n - round(sqrt_n)) < 1e-7:
        answer = (round(sqrt_n)+1)**2
    else:
        answer = -1
    
    return answer
