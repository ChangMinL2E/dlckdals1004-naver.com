# 암호 해독

'''
cipher	code	result
"dfjardstddetckdaccccdegk"	4	"attack"
"pfqallllabwaoclk"	2	"fallback"
'''

def solution(cipher, code):
    answer = ''
    for idx in range(code-1,len(cipher),code):
        answer += cipher[idx]
    return answer