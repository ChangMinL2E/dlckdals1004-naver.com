# 4366_2

for tc in range(1,int(input())+1):
    two = input()
    three = input()
    two_total = []
    three_total = []

    for idx in range(len(two)):
        if two[idx] == '0':
            two_total.append(two[:idx]+'1'+two[idx+1:])
        else:
            two_total.append(two[:idx]+'0'+two[idx+1:])

    for idx in range(len(three)):
        if three[idx] == '0':
            three_total.append(three[:idx] + '1' + three[idx + 1:])
            three_total.append(three[:idx] + '2' + three[idx + 1:])
        elif three[idx] == '1':
            three_total.append(three[:idx] + '0' + three[idx + 1:])
            three_total.append(three[:idx] + '2' + three[idx + 1:])
        elif three[idx] == '2':
            three_total.append(three[:idx] + '1' + three[idx + 1:])
            three_total.append(three[:idx] + '0' + three[idx + 1:])

    two_total = list(set(two_total))
    three_total = list(set(three_total))

    total = []
    for w in two_total:
        for h in three_total:
            if int(w,2) == int(h,3):
                total.append(int(w,2))

    print(f'#{tc}',*total)
