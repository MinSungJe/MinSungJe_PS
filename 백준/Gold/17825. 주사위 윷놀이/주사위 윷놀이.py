# 입력부
dice = list(map(int, input().split()))

# 지도 정보 입력
Map = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],
       [10, 13, 16, 19],
       [20, 22, 24],
       [30, 28, 27, 26],
       [25, 30, 35, 40, 0]]

# 말 초기값 선언
mark = [[0, 0] for _ in range(4)]

# DFS 완전탐색
def DFS(Mark, time, value):
    if time == 10: return value # 모든 주사위를 굴림

    # 다음 탐색
    max_value = 0
    for i in range(4):
        temp = [arr[:] for arr in Mark] # backtracking

        # 탐색 불가 조건
        if temp[i][0] == 4 and temp[i][1] == 4: continue # 이미 도착한 말임

        # 주사위 수치대로 이동시켜봄
        temp[i][1] += dice[time]

        # 각 경우마다 확인
        if temp[i][0] == 0:
            # 파란색 화살표 고려
            if temp[i][1] == 5:
                temp[i][0] = 1
                temp[i][1] = 0
            if temp[i][1] == 10:
                temp[i][0] = 2
                temp[i][1] = 0
            if temp[i][1] == 15:
                temp[i][0] = 3
                temp[i][1] = 0

            if temp[i][1] >= 20: # 범위를 벗어남
                temp[i][0] = 4
                temp[i][1] = 3 + (temp[i][1]-20)
        
        if temp[i][0] == 1:
            if temp[i][1] >= 4: # 범위를 벗어남
                temp[i][0] = 4
                temp[i][1] -= 4

        if temp[i][0] == 2:
            if temp[i][1] >= 3: # 범위를 벗어남
                temp[i][0] = 4
                temp[i][1] -= 3

        if temp[i][0] == 3:
            if temp[i][1] >= 4: # 범위를 벗어남
                temp[i][0] = 4
                temp[i][1] -= 4

        if temp[i][0] == 4:
            if temp[i][1] >= 5: # 범위를 벗어남
                temp[i][1] = 4
        
        # 도착지점에 말이 이미 있는지 여부 확인
        canMove = True
        for j in range(4):
            if temp[i][0] == 4 and temp[i][1] == 4: break # 도착한 경우는 판정 X
            if i == j: continue
            if temp[i][0] == temp[j][0] and temp[i][1] == temp[j][1]:
                canMove = False
                break
        if not canMove: continue

        # 탐색
        max_value = max(max_value, DFS(temp, time+1, value+Map[temp[i][0]][temp[i][1]]))

    return max_value

# 함수 호출 및 출력부
result = DFS(mark, 0, 0)
print(result)