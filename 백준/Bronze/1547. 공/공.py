# 입력부
M = int(input())

# 위치값 저장(pos[1] = 1번 컵의 위치)
pos = [0, 1, 2, 3]
for _ in range(M):
    X, Y = map(int, input().split())

    # 위치 변경
    temp = pos[X]
    pos[X] = pos[Y]
    pos[Y] = temp

# 출력부
for result in range(1, 4):
    if pos[result] == 1: print(result)