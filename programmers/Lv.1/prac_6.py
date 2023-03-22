# 하샤드 수

'''
arr	return
10	true
12	true
11	false
13	false
'''

def solution(x):
    answer = True
    
    test = 0
    for i in str(x):
        test+= int(i)
    
    if x % test == 0:
        return True
    else:
        return False
