# 입력부
N, K = map(int, input().split())
w = list(map(int, input().split()))

# 무게 정렬
w.sort()

# 투 포인터
l = 0
r = N-1
result = 0
while l < r:
    weight = w[l] + w[r]
    
    if weight <= K:
        result += 1
        l += 1
        r -= 1
    else: r -= 1

# 출력부
print(result)