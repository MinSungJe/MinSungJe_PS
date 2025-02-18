# 입력부
N = int(input())
leftPizza = list(map(int, input().split()))

# 돌아가며 피자 먹기
result = [-1 for _ in range(N)]
turn = N-1
idx = 0
while sum(leftPizza):
    # 턴 진행
    turn = (turn+1) % N

    if leftPizza[turn] == 0: continue
    leftPizza[turn] -= 1
    idx += 1

    # 마지막 피자 기록
    if leftPizza[turn] == 0 and result[turn] == -1: result[turn] = idx
    
# 출력부
print(*result)