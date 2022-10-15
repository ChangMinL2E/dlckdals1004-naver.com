# BOJ_1157 단어 공부  class 1

cnt_lst = [0]*26
InputS = list(input().lower())
for i in InputS:
    # print(ord(i))
    cnt_lst[ord(i)-97] += 1

max_idx = -1
maximum = 0
if cnt_lst.count(max(cnt_lst)) > 1:
    print('?')
else:
    print(chr(97+cnt_lst.index(max(cnt_lst))).upper())

