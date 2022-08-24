# 0824 Queue 구현

N = 10
Q = [-1]*N
front = rear = -1

def enqueue(item):
    global rear
    # if rear == N-1:
    #     rear = 0
    # else:
    #     rear += 1
    rear = (rear+1) % N
    Q[rear] = item

def dequeue():
    global front

    front = (front+1) % d
    return Q[front]

# 원형 큐에는 front와 rear 사이에 하나를 꼭 남겨준다.
# full인 경우 front와 rear의 차이가 하나.

# 스택에서.
Stk = []
Stk.append(item)
Stk.pop(-1)

# 큐에서
Q = []
Q.append(item)
Q.pop(0)


# Revisit to 마이쮸
numofCandy = 20
Q = []
No = 1
candy = [0] * numofCandy # 이렇게 해도 좋다.
# while ?? # 한번 생각해보고 해보는게 어떻는지.
remain = 20
while remain > 0:
    t = Q.pop(0)
    cnt[t] += 1
    remain -= cnt[t]
    Q.append(t)
    n += 1
    Q.append(n)
    print(t, '학생 =>' , cnt[t], Q)
