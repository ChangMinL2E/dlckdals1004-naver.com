# 올바른 괄호

'''
s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false
'''

def solution(s):
    answer = True
    sol = 0
    for i in s:
        if i == "(":
            sol += 1
        else:
            sol -= 1
        
        if sol < 0:
            answer = False
            break
            
    if sol != 0:
        answer = False
    
    return answer
