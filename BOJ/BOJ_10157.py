# BOJ.10157. 자리배정

C, R = map(int, input().split())
sol_idx = int(input())
Matrix = []
Matrix.append([100]*(C+2))
for _ in range(R):
    lst = [0] * C
    lst.insert(0,100)
    lst.append(100)
    Matrix.append(lst)
# Matrix = [[0] * C for _ in range(R)]
Matrix.append([100]*(C+2))

cnt = 0
x, y = 1, 1
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

a, b = R, 1
Gamma = [(-1, 0), (0, 1), (1, 0), (0, -1)]
Matrix[a][b] = (x, y)
out = '0'
cml = True
if sol_idx == 1:
    out = '1 1'
if C*R < sol_idx:
    cml = False

while cml:
    for i in range(2,sol_idx+1): # i = 2~42
        # if i == C * R+1:
        #     out = '0'
        #     break

        if Matrix[a + Gamma[cnt][0]][b + Gamma[cnt][1]] == 0:
            pass
        else:
            cnt = (cnt + 1) % 4

        Matrix[a + Gamma[cnt][0]][b + Gamma[cnt][1]] = (x + delta[cnt][0], y + delta[cnt][1])
        out = (x + delta[cnt][0], y + delta[cnt][1])
        x, y = x + delta[cnt][0], y + delta[cnt][1]
        a, b = a + Gamma[cnt][0], b + Gamma[cnt][1]

    if len(out) == 2:
        out = list(map(str,out))
        out = ' '.join(out)

    cml = False

print(out)
