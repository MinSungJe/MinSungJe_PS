# TC
T = int(input())
for _ in range(T):
    # 입력부
    N = int(input())
    X = list(map(int, input().split()))

    # 누적합 구하기
    sumX = [0 for _ in range(len(X))]
    sumX[0] = X[0]
    for i in range(1, len(X)): sumX[i] = sumX[i-1] + X[i]
    sumX = [0] + sumX

    # maximum subarray 구하기
    answer = -1000
    for i in range(len(X) + 1):
        for j in range(i+1, len(X) + 1): answer = max(answer, sumX[j] - sumX[i])
    
    # 출력부
    print(answer)