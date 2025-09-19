# 입력부
n = int(input())
ports = list(map(int, input().split()))

# 초기값 선언
MAX = 40001
DP = [0 for _ in range(n+1)]
LIS = [0]

# 포트 탐색
for port in ports:
    l = 0
    r = len(LIS)
    while l < r:
        mid = (l+r) // 2
        
        if port <= LIS[mid]:
            r = mid

        else:
            l = mid + 1

    if r >= len(LIS): LIS.append(port)
    else: LIS[r] = port

# 출력부
answer = len(LIS) - 1
print(answer)