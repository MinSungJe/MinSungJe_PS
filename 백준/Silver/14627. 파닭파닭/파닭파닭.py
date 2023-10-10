import sys
input = sys.stdin.readline

S, C = map(int, input().split())
pa = list(int(input()) for _ in range(S))

# 파닭에 넣을 수 있는 파의 양을 이분탐색
def find(target):
    l = 0
    r = 1000000000

    while l < r:
        m = (l+r+1)//2
        count = 0

        # 파 개수 계산
        for p in pa:
            count += p//m
        
        if count < target:
            r = m-1
        else:
            l = m
    return l

# 파닭에 넣는 파의 최댓값 탐색
chickenPa = find(C)

# 라면에 넣을 파 계산
result = sum(pa) - (chickenPa * C)
print(result)