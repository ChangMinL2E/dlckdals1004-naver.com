# BOJ_2447 별찍기-10 분할정복
# 갑을 못잡아서 풀다가 풀이보고, 이해하고, 다시 손코딩하고 짜보기.

def conquer(lst): # lst = [A,B,C]

    result = []
    for i in range(3*len(lst)): # 행 3배 증가.
        if i//len(lst) == 1:
            result.append(lst[i%len(lst)]+' '*len(lst)+lst[i%len(lst)]) # A+' '*len(A)+A
        else:
            result.append(lst[i%len(lst)]*3) # A*3,B*3,C*3

    return result



N = int(input())
cnt = 0
while N != 3:
    N //= 3
    cnt += 1
stars = ['***','* *','***']

for _ in range(cnt):
    stars = conquer(stars)

for star in stars:
    print(star)






