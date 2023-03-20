# 겹치는 선분의 길이

'''
lines	result
[[0, 1], [2, 5], [3, 9]]	2
[[-1, 1], [1, 3], [3, 9]]	0
[[0, 5], [3, 9], [1, 10]]	8
'''

def solution(lines):
    dic = {}
    for i in range(-100,101):
        dic[i] = 0
    
    for line in lines:
        for i in range(line[0],line[1]):
            dic[i] += 1
    # print(dic)
    answer = 0
    for key in dic.keys():
        # print(key)
        if dic[key] > 1:
            # print(key)
            answer += 1
    
    return answer