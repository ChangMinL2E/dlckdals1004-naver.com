# 로또의 최고 순위와 최저 순위

'''
lottos	win_nums	result
[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]
'''

def solution(lottos, win_nums):
    # 1-6, 2-5, 3-4, 4-3, 5-2, 6-1 or 6-0
    
    zeros = 0
    correct = 0
    for number in lottos:
        if int(number) == 0:
            zeros += 1
        else:
            if number in win_nums:
                correct += 1
                
    # 맞춘 갯수별 등수
    dic = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    maximum = dic[zeros+correct]
    minimum = dic[correct]

    answer = [maximum,minimum]
    return answer