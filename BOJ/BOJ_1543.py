# BOJ_1543 문서 검색

inputS = input()
word = input()

cml = True
cnt = 0
while cml:
    if len(inputS) < len(word):
        cml = False
    else:
        if inputS[:len(word)] == word:
            cnt += 1
            inputS = inputS[len(word):]
        else:
            inputS = inputS[1:]

print(cnt)