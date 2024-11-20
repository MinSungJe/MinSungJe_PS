# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 반대쪽을 알려주는 함수
def getOppositeIdx(idx):
    if idx == 2 or idx == 4: return 6-idx
    if idx == 0 or idx == 5: return 5-idx
    if idx == 1 or idx == 3: return 4-idx

# 가장 큰 값을 알려주는 함수
def getValue(top, bottom):
    if top == 6 or bottom == 6:
        if top == 5 or bottom == 5: return 4
        else: return 5
    return 6

# 입력부
N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

# 주사위 쌓기
result = 0
for start in range(6):
    value = 0
    idx = start
    for i in range(N):
        oppositeIdx = getOppositeIdx(idx)
        value += getValue(dice[i][idx], dice[i][oppositeIdx])
        
        # 다음 idx 찾기
        if i == N-1: continue
        for idx_ in range(6):
            if dice[i+1][idx_] == dice[i][oppositeIdx]: idx = idx_ 
    
    # 최댓값 기록
    result = max(result, value)

# 출력부
print(result)