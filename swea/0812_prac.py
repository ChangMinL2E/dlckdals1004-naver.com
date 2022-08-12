# 문자열 뒤집는 함수

def str_reverse(st):
    N = len(st)
    lst = list(st)
    for i in range(N//2):
        lst[i], lst[N-i-1] = lst[N-i-1], lst[i]

    return ''.join(lst)

print(str_reverse('abcd'))

