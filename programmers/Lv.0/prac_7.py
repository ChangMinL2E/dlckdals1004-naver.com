# 7의 개수

'''
array	result
[7, 77, 17]	4
[10, 29]	0
'''

def solution(array):
    answer = 0
    array = map(str,array)
    for ele in array:
        answer += ele.count('7')
    return answer