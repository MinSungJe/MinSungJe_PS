# 입력부
N = int(input())
balloons = list(map(int, input().split()))

# 초기값 선언
visited = [False for _ in range(N)]

# 풍선 터뜨리기
result = list()
idx = 0
for _ in range(N):
    # 풍선 터뜨림
    value = balloons[idx]
    result.append(idx+1)
    visited[idx] = True

    # 풍선 탐색
    count = 0
    while count < abs(value) and len(result) < N:
        # 터뜨릴 풍선 확인
        if value < 0: idx = ((idx-1) + N) % N
        else: idx = (idx+1) % N

        # 이미 터져있는 풍선임
        if visited[idx]: continue

        # 이동 횟수 기록
        count += 1

# 출력부
print(*result)