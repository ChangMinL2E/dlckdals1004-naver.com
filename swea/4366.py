# swea 4366. 정식이의 은행업무

def transform2(lst):
    N = len(lst)
    total = 0
    for i in range(N - 1, -1, -1):
        total += (2 ** (N - i - 1)) * int(lst[i])

    return total


def transform3(lst):
    N = len(lst)
    total = 0
    for i in range(N - 1, -1, -1):
        total += (3 ** (N - i - 1)) * int(lst[i])

    return total


for tc in range(1,int(input())+1):
    two_number = list(map(int,input()))
    three_number = list(map(int,input()))

    two_available = []
    three_available = []

    for i in range(len(two_number)):
        test_two = two_number[:]
        if test_two[i] == 0:
            test_two[i] = 1
        else:
            test_two[i] = 0
        two_available.append(transform2(test_two))

        for j in range(len(three_number)):
            test_three1 = three_number[:]
            test_three2 = three_number[:]
            if test_three1[j] == 0:
                test_three1[j] = 1
                three_available.append(transform3(test_three1))
            elif test_three1[j] == 2:
                test_three1[j] = 1
                three_available.append(transform3(test_three1))
            else:
                test_three1[j] = 2
                test_three2[j] = 0
                three_available.append(transform3(test_three1))
                three_available.append(transform3(test_three2))

            # if j == 1 and (transform2(test_two) == transform3(test_three1) or transform2(test_two) == transform3(test_three2)):
            #     two_number = test_two
            #     cml = True
            #     break
            # elif transform2(test_two) == transform3(test_three1):
            #
            #     two_number = test_two
            #     cml = True
            #     break

        # if cml:
        #     break
    # print(two_available)
    # print(three_available)


    two_available = set(two_available)
    three_available = set(three_available)
    sol = list(two_available & three_available)[0]
    #
    #
    print(f'#{tc} {sol}')



1
1010
212