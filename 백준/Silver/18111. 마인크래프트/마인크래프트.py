import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

time = -1
height = 0

# 목표높이 지정
for h in range(257):
    # 초기값 선언
    tmpTime = 0
    blocks = B
    for i in range(N):
        row = Map[i]
        for j in range(M):
            if row[j] > h: # 목표높이보다 큼
                breakBlocks = row[j] - h
                tmpTime += 2 * breakBlocks
                blocks += breakBlocks
            elif row[j] < h: # 목표높이보다 작음
                createBlocks = h - row[j]
                tmpTime += createBlocks
                blocks -= createBlocks

    # 남은 블럭이 음수가 아니라면 가능한 높이이다.
    if blocks >= 0 and (time == -1 or tmpTime <= time):
        time = tmpTime
        height = h

print(time, height)