# 카드 뭉치

'''
cards1	cards2	goal	result
["i", "drink", "water"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"Yes"
["i", "water", "drink"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"No"
'''

def solution(cards1, cards2, goal):
    answer = "No"
    while True:
        if goal == []:
            answer = 'Yes'
            break
        if len(cards1) > 0 and len(goal)>0 and cards1[0] == goal[0]:
            cards1 = cards1[1:]
            goal = goal[1:]
        elif len(cards2) > 0 and len(goal)>0 and cards2[0] == goal[0]:
            cards2 = cards2[1:]
            goal = goal[1:]
        else:
            break
    
    return answer


# def Backtracking(lst1, lst2, sol, answer):
    
#     if sol == []:
#         answer = 'Yes'
#         return
    
#     if len(lst1)>0 and len(sol)>0 and lst1[0] == sol[0]:
#         Backtracking(lst1[1:], lst2, sol[1:], answer)
        
#     if len(lst2)>0 and len(sol)>0 and lst2[0] == sol[0]:
#         Backtracking(lst1, lst2[1:], sol[1:], answer)


# print(solution(["i", "drink", "water"],	["want", "to"],	["i", "want", "to", "drink", "water"]))