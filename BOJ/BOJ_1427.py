# BOJ_1427 sort inside

InputS = input()
lst = sorted(map(int,list(InputS)), reverse=True)
InputS = ''.join(map(str,lst))

print(InputS)