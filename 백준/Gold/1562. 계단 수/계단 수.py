# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())

# 초기값 선언
DP = [[[-1 for _ in range(1<<10)] for _ in range(N)] for _ in range(10)]

# DFS(+DP)
def stair(number, length, visited):
    # 탐색 완료
    if length == N:
        if visited == (1<<10)-1 : return 1
        else: return 0

    # 메모이제이션
    if DP[number][length][visited] != -1: return DP[number][length][visited]

    
    count = 0
    for dn in (-1, 1):
        number_ = number + dn
        if number_ < 0 or number_ >= 10: continue # 탐색 불가 조건
        count += stair(number_, length+1, visited|1<<number_) # 탐색
        count = count % 1000000000
    
    DP[number][length][visited] = count
    return DP[number][length][visited]

# 함수 호출 및 출력부
result = 0
for i in range(1, 10):
    result += stair(i, 1, 1<<i)
    result = result % 1000000000
print(result)