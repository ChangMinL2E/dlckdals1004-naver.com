# BOJ_6603 로또 / Backtracking

def Backtracking(lst,k,N,pre_idx):
    if (N-pre_idx)+k < 6:
        return

    if k == 6:
        print(*lst)
        return

    for i in range(pre_idx+1,N):
        lst.append(InputLst[i])
        Backtracking(lst,k+1,N,i)
        lst.pop()

while True:
    InputS = input()
    if InputS == '0':
        break
    else:
        InputLst = list(map(int,InputS.split()))
        N = InputLst.pop(0)
        for idx in range(N-5):
            Backtracking([InputLst[idx]],1,N,idx)

        print()


