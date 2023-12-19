# 빠른 입력 및 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# 팰린드롬 확인 함수
def palin(start, end):
    # 탐색 완료
    if start >= end: return 1
    if DP[start][end] != -1: return DP[start][end] # 메모이제이션

    if board[start] == board[end]:
        DP[start][end] = 1 * palin(start+1, end-1)
    else:
        DP[start][end] = 0

    return DP[start][end]

# 입력부
N = int(input())
board = list(map(int, input().split()))
M = int(input())

# 초기값 선언
DP = [[-1 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    S, E = map(int, input().split())
    print(1 if palin(S-1, E-1) else 0) # 함수 호출 및 출력부