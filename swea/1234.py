# 1234. 비밀번호

for tc in range(1,11):
    cnt, security = input().split()
    pw_lst = []

    for pw in security:
        if len(pw_lst) == 0:
            pw_lst.append(pw)
        elif len(pw_lst) > 0 and pw_lst[-1] != pw:
            pw_lst.append(pw)
        else:
            pw_lst.pop()

    password = ''.join(pw_lst)

    print(f'#{tc} {password}')
