# 입력부
N = int(input())
point_input = [list(map(int, input().split())) for _ in range(N)]
points = [list() for _ in range(N+1)]

# 입력값 정렬 후 points 배열에 넣기
point_input.sort()
for x, y in point_input:
    points[y].append(x)

# 결과값 계산
result = 0
for dots in points:
    length = len(dots)
    for i in range(length):
        if i == 0:
            result += (dots[i+1]-dots[i])
            continue
        if i == length-1:
            result += (dots[i]-dots[i-1])
            continue
        result += min((dots[i+1]-dots[i]), (dots[i]-dots[i-1]))

# 출력부
print(result)