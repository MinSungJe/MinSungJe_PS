# 입력부
N, M, R = map(int, input().split())
piles = list(map(int, input().split()))
flags = list(map(int, input().split()))

# 정렬
piles.sort()
flags.sort()

# 초기값 선언
result = -1

# 해당 넓이 이상으로 현수막을 만들 수 있는지 확인하는 함수
def canFlag(size):
    for flag in flags:
        i = 0
        j = 0
        while i != N-1 and j < N:
            area = (piles[j]-piles[i]) * flag
            if area <= R*2 and area >= size:
                return True
            if area > R*2:
                i += 1
            if area < size:
                j += 1
    return False

# 이분탐색 알고리즘
l = 1
r = (R+1)*2
while l < r:
    m = (l+r)//2

    if canFlag(m):
        result = m/2
        l = m + 1
    else:
        r = m

# 출력부
print(f"{result:.1f}" if result != -1 else -1)