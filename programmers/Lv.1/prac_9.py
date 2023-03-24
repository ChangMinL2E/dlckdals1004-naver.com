# K번째수

'''
array	commands	return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
'''

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command[0]-1,command[1],command[2]-1
        answer.append(sorted(array[i:j])[k])
    
    return answer