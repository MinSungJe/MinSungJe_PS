# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 하트 아트인지 확인하는 함수
def isHeart(Coffee):
    # 길이 확인
    N = len(Coffee)

    # 4방향 확인
    count, startX, startY = 0, 0, 0
    for x, y in [(0, 0), (0, N-1), (N-1, 0), (N-1, N-1)]:
        if Coffee[x][y] == '.':
            count += 1
            startX, startY = x, y
    if count != 1: return False

    # 처음 시작 위치에 따라 검사하는 범위가 달라짐
    if startX == 0:
        if startY == 0:
            # 커피 길이 확인
            M = 0
            for i in range(N):
                if Coffee[startX][i] == '#': break
                else: M += 1
            
            # 검사
            for x in range(N):
                for y in range(N):
                    if (x < M and y < M):
                        if Coffee[x][y] == '#': return False
                    else:
                        if Coffee[x][y] == '.': return False

        if startY == N-1:
            # 커피 길이 확인
            M = 0
            for i in range(N-1, -1, -1):
                if Coffee[startX][i] == '#': break
                else: M += 1

            # 검사
            for x in range(N):
                for y in range(N):
                    if (x < M and y >= N-M):
                        if Coffee[x][y] == '#': return False
                    else:
                        if Coffee[x][y] == '.': return False

    if startX == N-1:
        if startY == 0:
            # 커피 길이 확인
            M = 0
            for i in range(N):
                if Coffee[startX][i] == '#': break
                else: M += 1
            
            # 검사
            for x in range(N):
                for y in range(N):
                    if (x >= N-M and y < M):
                        if Coffee[x][y] == '#': return False
                    else:
                        if Coffee[x][y] == '.': return False

        if startY == N-1:
            # 커피 길이 확인
            M = 0
            for i in range(N-1, -1, -1):
                if Coffee[startX][i] == '#': break
                else: M += 1

            # 검사
            for x in range(N):
                for y in range(N):
                    if (x >= N-M and y >= N-M):
                        if Coffee[x][y] == '#': return False
                    else:
                        if Coffee[x][y] == '.': return False
    return True

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    R, C = map(int, input().split())
    Map = [list(input()) for _ in range(R)]

    # 초기값 선언
    result = False

    # 크림 부분 축소
    left, right, top, bottom = 11, 11, 11, 11
    for x in range(R):
        count = 0
        for y in range(C):
            if Map[x][y] == '#': break
            else: count += 1
        left = min(left, count)

        count = 0
        for y in range(C-1, -1, -1):
            if Map[x][y] == '#': break
            else: count += 1
        right = min(right, count)

    for y in range(C):
        count = 0
        for x in range(R):
            if Map[x][y] == '#': break
            else: count += 1
        top = min(top, count)
        
        count = 0
        for x in range(R-1, -1, -1):
            if Map[x][y] == '#': break
            else: count += 1
        bottom = min(bottom, count)

    Art = list()
    for x in range(top, R-bottom):
        Art.append(Map[x][left:C-right])

    # 자른 부분이 정사각형인 경우 하트아트인지 확인
    if Art:
        X, Y = len(Art), len(Art[0])
        if X == Y: result = isHeart(Art)

    # 출력부
    print(1 if result else 0)