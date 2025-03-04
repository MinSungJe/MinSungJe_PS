# 입력부
N = int(input())
M = int(input())
stuff = list(map(int, input().split()))

# 재료 정렬
stuff.sort()

# 투포인터
l = 0
r = N-1
result = 0
while l < r:
    value = stuff[l] + stuff[r]
    if value > M: r -= 1
    elif value == M:
        result += 1
        l += 1
        r -= 1
    else: l += 1

# 출력부
print(result)