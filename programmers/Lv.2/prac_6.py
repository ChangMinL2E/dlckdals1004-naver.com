from itertools import permutations


def solution(numbers):
    answer = ''
    
    lst = list(map(list,list(permutations(numbers))))
    for ls in lst:
        ls = list(map(str,ls))
        ls = ''.join(ls)
        
    print(lst)
    
    return answer

print(solution([6,10,2]))