# 새로운 버스 노선
# 아직 수정후에 디버깅을 못했다.

for tc in range(1, int(input()) + 1):
    N = int(input()) 
    lst = []
    for i in range(N): 
        lst.append([]) # 2차원 배열 원소로 N개 행렬 생성
    
    total_ele = []

    for j in range(N): 
        C, A, B = map(int, input().split())
        if C == 1:
            for num1 in range(A, B + 1):
                lst[j].append(num1)
                total_ele.append(num1)
        elif C == 2:
            if A % 2 == 0:
                for num2 in range(A, B, 2):
                    lst[j].append(num2)
                    total_ele.append(num)
                if B not in lst2:
                    lst[j].append(B)
                    total_ele.append(num)
            else:
                for num2 in range(A, B, 2):
                    lst[j].append(num2)
                    total_ele.append(num)
                if B not in lst2:
                    lst[j].append(B)
                    total_ele.append(num)
        else:
            if A % 2 == 0:
                for num3 in range(A, B):
                    if num3%4 == 0:
                        lst[j].append(num3)
                        total_ele.append(num)
                if B not in lst3:
                    lst[j].append(B)
                    total_ele.append(num)
            else:
                for num3 in range(A, B):
                    if num3%10:
                        lst[j].append(num3)
                        total_ele.append(num)
                if B not in lst3:
                    lst[j].append(B)
                    total_ele.append(num)


    total = list(set(total_ele))

    maximum = 0
    total_num = 0

    for num in total_ele:
        for ls in lst:
            if num in ls:
                total_num += 1
        if maximum < total_num:
            maximum = total_num

    print(f'#{tc} {total_num}')