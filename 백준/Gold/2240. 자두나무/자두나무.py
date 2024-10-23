# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
T, W = map(int, input().split())
jadu = [int(input()) for _ in range(T)]

# DP 배열 선언
DP = [[[-1 for _ in range(W+1)] for _ in range(3)] for _ in range(T)]

# DFS
def DFS(idx, pos, move):
    # 탐색 종료
    if idx == T: return 0
    if DP[idx][pos][move] != -1: return DP[idx][pos][move] # 메모이제이션

    # 다음 탐색
    result = 0
    jadu_eat = 1 if jadu[idx] == pos else 0

    # 자두나무 멈춤 or 이동
    result = max(result, jadu_eat+DFS(idx+1, pos, move))
    if move < W: result = max(result, jadu_eat+DFS(idx+1, 3-pos, move+1))

    DP[idx][pos][move] = result # 메모이제이션
    return result

# 함수 호출 및 출력부
result = max(DFS(0, 1, 0), DFS(0, 2, 1))
print(result)