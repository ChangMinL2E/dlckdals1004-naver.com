# 새로운 버스 노선
# 아직 수정후에 디버깅을 못했다.

for tc in range(1, int(input()) + 1):
    N = int(input()) 
    dic = {}
    for key in range(1,1001):
        dic[key] = 0 # count용 dic 생성

    for _ in range(N):
        lst = []
        C, A, B = map(int, input().split())
        if C == 1:
            for num1 in range(A, B + 1):
                lst.append(num1)
        elif C == 2:
            if A % 2 == 0:
                for num2 in range(A, B, 2):
                    lst.append(num2)
                if B not in lst:
                    lst.append(B)
            else:
                for num2 in range(A, B, 2):
                    lst.append(num2)
                if B not in lst:
                    lst.append(B)
        else: # C == 3 이면,
            if A % 2 == 0:
                for num3 in range(A, B):
                    if num3%4 == 0:
                        lst.append(num3)
                if B not in lst:
                    lst.append(B)
                if A not in lst:
                    lst.append(A)
            else:
                for num3 in range(A, B):
                    if num3%3==0 and num3%10:
                        lst.append(num3)
                if B not in lst:
                    lst.append(B)
                if A not in lst:
                    lst.append(A)

        for i in lst:
            dic[i] += 1
        

    maximum = 0

    for key in dic:
        if dic[key] > maximum:
            maximum = dic[key]

    print(f'#{tc} {maximum}')