# 기능개발 72.7

'''
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
'''

def solution(progresses, speeds):
    answer = []
    lst = list(map(lambda x: round((100-x)/speeds[progresses.index(x)]),progresses))
    maximum = lst[0]
    cnt = 0
    for i in range(len(lst)+1):
        if i == 0:
            cnt += 1
            maximum = lst[0]
        elif 0 < i and i < len(lst):
            if lst[i] <= maximum:
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1
                maximum = lst[i]
                
        if i == len(lst):
            answer.append(cnt)
    return answer

# print(solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]	))