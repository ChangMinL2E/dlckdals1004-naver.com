# BOJ_10872 재귀 팩토리얼

def fac(r):
    if r == 0:
        return 1
    else:
        return fac(r-1)*r

print(fac(int(input())))





