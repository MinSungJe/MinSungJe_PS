# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())

# 초기값 선언
INF = 1000000007

# DP 배열 선언
DP = [-1 for _ in range(N+1)]

# DFS
def DFS(idx):
    if idx > N: return 1
    if DP[idx] != -1: return DP[idx]

    # 값 구하기
    result = 0
    result = (result + 2*DFS(idx+1)) % INF
    result = (result + DFS(idx+1)) % INF
    result %= INF
    
    # 메모이제이션
    DP[idx] = result
    return result

# 함수 호출 및 출력부
result = DFS(1)
print(result-1)