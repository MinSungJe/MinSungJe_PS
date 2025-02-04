# 입력부
N = int(input())

# 초기값 선언
minX, maxX, minY, maxY = 11, -11, 11, -11

# 건물 입력받으며 울타리 비용 출력
for _ in range(N):
    a, b, c, d = map(int, input().split())
    minX = min(minX, a)
    maxX = max(maxX, c)
    minY = min(minY, b)
    maxY = max(maxY, d)

    # 울타리 비용 계산 및 출력부
    result = 2 * (maxX-minX) + 2 * (maxY-minY)
    print(result)