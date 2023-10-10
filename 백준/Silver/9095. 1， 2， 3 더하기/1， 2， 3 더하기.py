T = int(input())
for test_case in range(1,T+1):
    # 입력부
    n = int(input())
    
    # DP배열 선언
    DP = [0 for _ in range(n+1)]
    DP[0] = 1 # (아무 것도 없는 경우 1가지)
    DP[1] = 1 # 1
    if n >= 2: DP[2] = 2 # 1+1, 2

    # DP배열 채우기
    for i in range(3,n+1): DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    # 결과값 출력
    print(DP[n])