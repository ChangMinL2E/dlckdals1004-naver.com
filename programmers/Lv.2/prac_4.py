# 프린터

'''
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5
'''

def solution(priorities, location):
    answer = 0
    new_pri = priorities[:]
    # 원소 : (중요도, 인덱스)
    lst = []
    for idx in range(len(priorities)):
        lst.append((priorities[idx],idx))
    
    while True:
        q = lst.pop(0)
        if q[0] == max(new_pri):
            new_pri[q[1]] = 0
            answer += 1
            if location == q[1]:
                break
        else:
            lst.append(q)
            
    return answer

print(solution([1, 1, 9, 1, 1, 1],	0))