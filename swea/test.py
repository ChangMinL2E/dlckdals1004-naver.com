# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
#
# print(s1==s2, s1 is s2)
# print(s1==s3, s1 is s3)
# print(s1==s4, s1 is s4)
# print(s1==s5, s1 is s5)

# def strcmp(st1,st2):
#     if st1 < st2:
#         return -1
#     if st1 == st2:
#         return 0
#     else:
#         return 1
#
# print(ord('0'))

# def atoi(s):
#     i = 0
#     for x in s:
#         i = i*10 + ord(x)-ord('0')
#     return i
#
# s = '123'
# a = atoi(s)
# print(a+1)

# print(chr(49))
def itoa(integer): # 숫자열을 받으면 문자열로 출력하기.
    lst = []

    if integer > 0:
        while integer != 0:
            lst.append(chr(integer%10 + 48))
            integer = integer//10

        for i in range(len(lst)//2):
            lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]
        s2 = ''.join(lst)

    elif integer < 0:
        integer = -integer
        while integer != 0:
            lst.append(chr(integer%10 + 48))
            integer = integer//10

        lst.append('-')
        for i in range(len(lst)//2):
            lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]
        s2 = ''.join(lst)

    else:
        s2 = '0'

    return s2


print(itoa(-458))
print(itoa(9568))
print(itoa(457))

# # 패턴 매칭
# if t[i] != p[j]:
#     i -= j
#     j = -1

# else:
#     i += 1
#     j += 1

