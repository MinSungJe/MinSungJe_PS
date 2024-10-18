# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())

# 초기값 선언
INF = 1000000

# DP 배열 선언
DP = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(N)]

# DFS
def DFS(idx, L, A):
    # 탐색 종료
    if L >= 2: return 0
    if A >= 3: return 0
    if idx >= N: return 1

    # 메모이제이션
    if DP[idx][L][A] != -1: return DP[idx][L][A]

    # 다음 탐색
    result = 0
    # 다음 일수를 출석 / 지각 / 결석
    for L_, A_ in ((L, 0), (L+1, 0), (L, A+1)):
        result += DFS(idx+1, L_, A_)
        result %= INF
    
    # 메모이제이션
    DP[idx][L][A] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 0, 0)
print(result)