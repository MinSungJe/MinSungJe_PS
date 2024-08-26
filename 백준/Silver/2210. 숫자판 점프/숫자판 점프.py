# 입력부
Map = [list(map(int, input().split())) for _ in range(5)]

# 초기값 선언
result = set()
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 초기 위치에서 탐색하는 함수
def makeNumber(X, Y, numbers):
    # 탐색 종료
    if len(numbers) == 6:
        result.add(numbers)
        return

    # 다음 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        # 탐색 불가 조건
        if X_ < 0 or X_ >= 5 or Y_ < 0 or Y_ >= 5: continue

        # 탐색
        makeNumber(X_, Y_, numbers+str(Map[X][Y]))

# 모든 위치에서 시작
for x in range(5):
    for y in range(5):
        makeNumber(x, y, '')

# 출력부
print(len(result))