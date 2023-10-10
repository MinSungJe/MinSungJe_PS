from collections import deque
T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    numlist = deque(list(map(int,input().split())))
    printlist = numlist.copy()
    sqlist = [0] * N

    target = max(printlist)
    idx = 1
    while not sqlist[M]:
        for i in range(N):
            if target == numlist[i] and not sqlist[i]:
                sqlist[i] = idx
                idx += 1
                printlist[i] = 0
                target = max(printlist)

    
    print(sqlist[M])