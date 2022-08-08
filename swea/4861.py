# 회문 가로 세로.

T = int(input())
for tc in range(1,T+1):
    lst = []
    num1, num2 = map(int,input().split())

    
    for _ in range(num1):
        lst.append(input()) # 들어오는 문자열을 list.append
    # lst 는 num1 X num1 행렬
    sol = []

    for ls in lst: # 행을 가져오겠다.
        for j in range(num1-num2+1): # num1-num2+1 만큼 비교해주겠다.
            if ls[j:j+num2] == ls[j:j+num2][::-1]: # 중앙값 기준 대칭되는 값 비교
                sol.append(ls)

    # 열 대칭 회문 찾기.
    for j in range(num1-num2+1): # 전치행렬은 복잡하고,
        for i in range(len(lst)): # 인덱스로 하자!
            sol_lst = []
            for k in range(num2):
                sol_lst.append(lst[j+k][i]) # 열 별로 원소 추가.
            if sol_lst == sol_lst[::-1]:
                sol.append(''.join(sol_lst))
            
    print(f'#{tc} {str(sol[0])}')

