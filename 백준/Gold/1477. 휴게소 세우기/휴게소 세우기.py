# 입력부
N, M, L = map(int, input().split())
if N: rest = list(map(int, input().split())) + [L]
else: rest = [L]
rest.sort()

# 주어진 조건이 가능한 지 확인하는 함수
def isPossible(dist, count):
    last_rest = 0
    c = 0
    for i in range(N+1):
        while True:
            value = rest[i] - last_rest
            if value <= dist:
                last_rest = rest[i]
                break
            c += 1
            last_rest += dist

    if c > count: return False
    else: return True

# 이분 탐색
def BS(dist):
    result = 101
    l = 0
    r = 101
    while l < r:
        m = (l+r) // 2        
        if isPossible(dist, m):
            result = min(result, m)
            r = m
        else: l = m+1

    return result

# 함수 호출 및 출력부
for dist in range(1, 1001):
    if BS(dist) <= M:
        result = dist
        break
print(result)