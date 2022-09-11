# BOJ_25501 재귀의 귀재

def isPalindrome(S):
    global cnt

    if len(S)==1 or len(S)==0:
        return 1
    elif S[0]==S[-1]:
        cnt += 1
        return isPalindrome(S[1:-1])
    else:
        return 0

for _ in range(int(input())):
    cnt = 1
    print(isPalindrome(input()), cnt)


