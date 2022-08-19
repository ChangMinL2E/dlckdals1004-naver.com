TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    result = ''
    if N%2:
        result = 'Bob'
    else:
        result = 'Alice'

    print(f'#{tc} {result}')