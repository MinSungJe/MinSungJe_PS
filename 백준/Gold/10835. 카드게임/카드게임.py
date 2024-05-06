# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())
left_card = list(map(int, input().split()))
right_card = list(map(int, input().split()))

# DP 배열 선언
DP = [[-1 for _ in range(N)] for _ in range(N)]

# DFS(+DP)
def DFS(left, right):
    if left == N or right == N: return 0
    if DP[left][right] != -1: return DP[left][right]

    # 다음 탐색
    result = 0
    if left_card[left] > right_card[right]: result = max(result, right_card[right]+DFS(left, right+1))
    else: result = max(result, DFS(left+1, right), DFS(left+1, right+1))

    DP[left][right] = result # 메모이제이션
    return result

# 함수 호출 및 출력부
result = DFS(0, 0)
print(result)