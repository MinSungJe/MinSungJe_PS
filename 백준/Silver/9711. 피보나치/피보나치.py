# 테스트 케이스
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    P, Q = map(int, input().split())
        
    # DP 배열 선언
    DP = [0 for _ in range(P+1)]
    DP[1] = 1 % Q
    for i in range(2, P+1): DP[i] = (DP[i-1] + DP[i-2]) % Q
    
    # 출력부
    print(f"Case #{test_case}: {DP[P]}")