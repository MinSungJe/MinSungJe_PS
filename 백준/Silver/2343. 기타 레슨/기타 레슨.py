# 입력부
N, M = map(int, input().split())
video = list(map(int, input().split()))

# 주어진 블루레이 크기로 나눌 수 있는지 확인
def canDivide(size):
    idx = 0
    value = 0
    section = 1
    while idx < N:
        if value + video[idx] <= size:
            value += video[idx]
            idx += 1
            continue
        
        # 구역이 나뉨
        section += 1
        value = 0
        if section > M: return False # 나눌 수 있는 최대치 초과
    
    return True

# 이분 탐색
INF = 1000000000
start = 0
end = INF
result = INF
while start < end:
    mid = (start+end) // 2

    if canDivide(mid):
        result = mid
        end = mid
    else: start = mid+1

# 출력부
print(result)