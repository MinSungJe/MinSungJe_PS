def solution(n):
    answer = 0
    # DP Table 선언
    DP = [0 for _ in range(n+1)]
    DP[0] = 1
    DP[1] = 1
    
    # DP Table 채우기
    for i in range(2, n+1):
        temp = 0
        for j in range(i):
            temp += DP[j] * DP[i-(j+1)]
        DP[i] = temp
    
    # 출력부
    answer = DP[n]
    return answer