# 입력부
N = int(input())
weights = list(map(int, input().split()))

# 추 무게 정렬
weights.sort()

# 측정할 수 있는 무게와 추 무게 비교
K = 0
for W in weights:
    if K+1 < W:
        result = K+1
        break
    K = K+W

# 출력부
result = K+1
print(result)