# BOJ_9299 Math Tutoring

for _ in range(int(input())):
    lst = list(map(int,input().split()))

    sol = []
    first = lst.pop(0)
    if first == 0:
        # lst.pop(0)
        sol.append(0)
        sol.append(0)

    else:
        sol.append(first-1)
        for i in range(len(lst) - 1):
            sol.append((len(lst) - i - 1) * lst[i])

    # for i in range(len(lst)-1):
    #     sol.append((len(lst)-i-1)*lst[i])
    output = ''
    for so in sol:
        output += str(so) + ' '
    print(f'Case {_+1}:', output)