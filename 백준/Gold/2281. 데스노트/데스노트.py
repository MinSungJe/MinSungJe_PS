# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
n, m = map(int, input().split())
names = [int(input()) for _ in range(n)]

# 초기값 선언
INF = 1000000001
DP = [[-1 for _ in range(m+1)] for _ in range(n)]

# DFS
def DFS(idx, pos):
    # 탐색 종료
    if idx >= n: return 0
    if pos > m: return INF

    # 메모이제이션
    if DP[idx][pos] != -1: return DP[idx][pos]

    # 다음 탐색
    result = INF
    value = m-pos-names[idx]
    if value < 0: return INF
    result = min(result, value**2+DFS(idx+1, 0), DFS(idx+1, pos+names[idx]+1))

    DP[idx][pos] = result # 메모이제이션
    return result

# 함수 호출 및 출력부
result = DFS(0, 0)
print(result)