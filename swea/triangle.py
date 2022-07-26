
lst = []

for i in range(8):
    if i == 7:
        print('*'*15)
    elif i == 0:
        str = ' '*7+'*'+' '*7
        print(str)
    else:
        lst = [' ']*15
        lst[7-i] = '*'
        lst[7+i] = '*'
        lst_st = ''.join(lst)
        print(lst_st)




