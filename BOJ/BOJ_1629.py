# BOJ_1629 곱셈

A,B,C = map(int,input().split())

def divide(number):
    if number == 1:
        return A%C
    else:
        if number%2 == 0:
            return divide(number//2)*divide(number//2)%C
        else:
            return divide(number//2)*divide(number//2)*A%C

print(divide(B))




