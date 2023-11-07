# 입력부
N, M, R = map(int, input().split())
piles = list(map(int, input().split()))
flags = list(map(int, input().split()))

# 정렬
piles.sort()
flags.sort()

# 초기값 선언
result = 0

# 간격 배열 선언
width = set()
for i in range(N):
    for j in range(i,N):
        width.add(piles[j]-piles[i])
width = sorted(list(width))

# 이분탐색 알고리즘
def BS(w):
    global result

    l = 0
    r = M-1
    while l <= r:
        m = (l+r)//2
        area = w * flags[m] / 2
        if area > R:
            r = m-1
        else:
            result = max(area, result)
            l = m+1

# 출력부
for w in width:
    BS(w)
print(f"{result:.1f}" if result else -1)