# BOJ_1213 팰림드롬 만들기

import sys
input = sys.stdin.readline

dic = {}
InputS = input().strip()
Lst = list(InputS)
set_Lst = sorted(list(set(Lst)))
cnt = 0
for ls in set_Lst:
    dic[ls] = Lst.count(ls)
    if Lst.count(ls)%2:
        cnt += 1

    if cnt >=2 :
        print("I'm Sorry Hansoo")
        break

result = ''
if cnt < 2:
    if not cnt:
        for ls in set_Lst:
            result += ls*(dic[ls]//2)

        result = result+result[::-1]
        print(result)
    else:
        me = ''
        for ls in set_Lst:
            if dic[ls]%2:
                me = ls
            result += ls * (dic[ls] // 2)
        result2 = result[:]
        result += me

        result += result2[::-1]
        print(result)





