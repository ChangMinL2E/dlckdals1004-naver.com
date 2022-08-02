def con(num, C):
    count = 0
    cml = True
    l = 1
    r = C
    while cml:
        c = int((l+r)/2)
        if c == num:
            count += 1
            cml = False
        else:
            count += 1
            if c > num:
                r = c
            else:
                l = c
    return count

print(con(200,400))