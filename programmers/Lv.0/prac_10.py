# 유한소수 판별하기

'''
a	b	result
7	20	1
11	22	1
12	21	2
'''

def solution(a, b):
    answer = 1
    
    gcd = 1
    # 최대 공약수 구하기
    for i in range(min(a,b),0,-1):
        if not a%i and not b%i:
            gcd = i
            break
    new_b = b//i
    
    while True:
        if new_b == 1:
            break
        elif not new_b % 2:
            new_b = new_b//2
        elif not new_b % 5:
            new_b = new_b // 5
        else:
            answer = 2
            break
    
    return answer