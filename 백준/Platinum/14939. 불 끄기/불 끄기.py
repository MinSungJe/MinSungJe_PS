# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력값 정리
input_data = [list(input()) for _ in range(10)]
preMap = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        if input_data[i][j] == 'O': preMap[i][j] = 1

# 초기값 선언
dx = (0, -1, 1, 0, 0)
dy = (0, 0, 0, -1, 1)
INF = 101

# 스위치 누르는 함수
def switch(X, Y, M):
    Map = [arr[:] for arr in M]
    for i in range(5):
        X_, Y_ = X+dx[i], Y+dy[i]
        if X_ < 0 or X_ >= 10 or Y_ < 0 or Y_ >= 10: continue
        Map[X_][Y_] = 1-Map[X_][Y_]

    return Map

# 첫 줄을 누르는 모든 경우의 수 확인(비트마스킹)
result = INF
for case in range(1<<10):
    count = 0
    Map = [arr[:] for arr in preMap]
    for y in range(10):
        if case & (1<<y):
            Map = switch(0, y, Map)
            count += 1
    
    # 다음 줄부터, 위 전구가 켜져 있다면 스위치 누르기
    for x in range(1, 10):
        for y in range(10):
            if Map[x-1][y]:
                Map = switch(x, y, Map)
                count += 1
    
    # 마지막 줄 확인하고, 모두 꺼져있다면 결과값 반영
    if not any(Map[9]): result = min(result, count)

# 출력부
print(result)