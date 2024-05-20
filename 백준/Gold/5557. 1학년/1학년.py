# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())
numbers = list(map(int, input().split()))

# 메모이제이션
DP = [[-1 for _ in range(21)] for _ in range(N)]

# DFS
def DFS(idx, value):
    # 마지막 도착
    if idx == N-2:
        if numbers[idx]:
            if value+numbers[idx] == numbers[idx+1]: return 1
            if value-numbers[idx] == numbers[idx+1]: return 1
            return 0
        else:
            if value == numbers[idx+1]: return 2
            return 0

    # 메모이제이션 확인
    if DP[idx][value] != -1: return DP[idx][value]

    # 탐색
    result = 0
    for m in (-1, 1):
        value_ = value + (m*numbers[idx])

        # 탐색 불가 조건
        if not idx and m == -1: continue # 처음엔 무조건 + 고정
        if value_ < 0 or value_ > 20: continue # 난 음수랑 21이상 숫자 몰라요
        
        result += DFS(idx+1, value_)

    # 메모이제이션
    DP[idx][value] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 0)
print(result)