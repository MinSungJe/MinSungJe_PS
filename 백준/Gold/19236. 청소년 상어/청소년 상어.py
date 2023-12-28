# 입력부
info = [list(map(int, input().split())) for _ in range(4)]
Map = [list() for _ in range(4)]
D = [list() for _ in range(4)]

# info 정리
for i in range(4):
    for j in range(0, 8, 2):
        Map[i].append(info[i][j])
        D[i].append(info[i][j+1])

# 초기값 설정
dx = (0, -1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 0, -1, -1, -1, 0, 1, 1, 1)

# 물고기 이동
def moveFish(M, D):
    M_ = [arr[:] for arr in M]
    D_ = [arr[:] for arr in D]

    for fish in range(1, 17):
        move = False
        for X in range(4):
            for Y in range(4):
                if M_[X][Y] == fish:                    
                    while not move:
                        X_ = X + dx[D_[X][Y]]
                        Y_ = Y + dy[D_[X][Y]]
                        # 이동 불가 조건
                        if X_ < 0 or X_ >= 4 or Y_ < 0 or Y_ >= 4 or M_[X_][Y_] == -1:
                            D_[X][Y] += 1
                            if D_[X][Y] > 8: D_[X][Y] -= 8
                            continue
                            
                        # 이동
                        fish1 = (M_[X][Y], D_[X][Y])
                        fish2 = (M_[X_][Y_], D_[X_][Y_])
                        M_[X][Y], D_[X][Y] = fish2
                        M_[X_][Y_], D_[X_][Y_] = fish1
                        move = True
                if move: break
            if move: break
    
    return M_, D_

# solution
def solution(X, Y, m, d):
    M = [arr[:] for arr in m]
    D = [arr[:] for arr in d]

    # 탐색 종료 조건
    if X < 0 or X >= 4 or Y < 0 or Y >= 4: return 0

    # 잡아먹음
    result = 0
    result += M[X][Y]
    M[X][Y] = -1
    if D[X][Y]: direction = D[X][Y]
    else: return 0
    D[X][Y] = 0

    # 물고기 이동
    M, D = moveFish(M, D)
    M[X][Y] = 0

    # 상어 이동
    max_value = 0
    for i in range(1,4):
        X_ = X + (dx[direction] * i)
        Y_ = Y + (dy[direction] * i)
        max_value = max(max_value, solution(X_, Y_, M, D))
    
    result += max_value

    return result

# 출력부
result = solution(0, 0, Map, D)
print(result)