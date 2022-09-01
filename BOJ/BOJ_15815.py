# BOJ_15815.py 천재 성필이

InputS = input()
numbers = '0123456789'

stk = []

for inputs in InputS:
    if inputs in numbers:
        stk.append(int(inputs))
    else:
        b = stk.pop()
        a = stk.pop()
        if inputs == '+':
            stk.append(a+b)
        elif inputs == '-':
            stk.append(a-b)
        elif inputs == '*':
            stk.append(a*b)
        else:
            stk.append(a/b)
print(stk[0])

