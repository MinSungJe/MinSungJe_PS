# 입력부
X1, Y1, X2, Y2, X3, Y3, X4, Y4 = map(int, input().split())

# 초기값 선언
point = [(X1, Y1), (X2, Y2), (X3, Y3), (X4, Y4)]
INF = 20001
minX = min(X1, X2, X3, X4)
minY = min(Y1, Y2, Y3, Y4)
maxX = max(X1, X2, X3, X4)
maxY = max(Y1, Y2, Y3, Y4)

# 4조각으로 나뉘는지 검사
result = 1

# 네 점 중 일치하는 점이 있을 경우
for i in range(4):
    for j in range(4):
        if i == j: continue
        if point[i][0] == point[j][0] and point[i][1] == point[j][1]: result = 0

# 일치하는 점이 없는 경우
if result:
    # 그래프식 구하기
    if X1 != X2: A1 = (Y2-Y1) / (X2-X1)
    else: A1 = INF
    if X3 != X4: A2 = (Y4-Y3) / (X4-X3)
    else: A2 = INF
    B1 = Y1 - (A1 * X1)
    B2 = Y3 - (A2 * X3)
    
    if A1 == A2: result = 0 # 선분이 평행한 경우(일치하는 경우도 걸러짐)
    else:
        # 만나는 점 구하기
        X = -1 * (B1-B2) / (A1-A2)
        Y = A1*X + B1

        # 만나는 점이 피자 밖에 있을 경우
        if X <= minX or X >= maxX or Y <= minY or Y >= maxY: result = 0

# 출력부
print(result)