# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, C = map(int, input().split())
Map = []
for _ in range(N):
    Map.append(int(input()))

# 집 위치 정렬
Map.sort()

# 최대 거리를 인자로 받고 배치가 가능한지 여부를 확인하는 함수
def install(dist):
    lastPos = Map[0]
    count = 1
    for pos in Map[1:]:
        if pos >= lastPos+dist:
            count += 1
            lastPos = pos
            if count == C: return True
    return False

# 이분탐색 알고리즘
def BS():
    l = 1
    r = Map[-1] - Map[0] + 1
    result = 0

    while l < r:
        m = (l+r)//2
        if install(m):
            l = m + 1
            result = m
        else:
            r = m

    # 출력부
    print(result)

# 함수 실행
BS()