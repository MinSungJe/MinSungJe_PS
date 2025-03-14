# 입력부
A, B, C, X, Y = map(int, input().split())

# 반반치킨 구성을 하나씩 늘리며 확인
max_chicken = max(X, Y)

result = 1000000001
for ban in range(max_chicken+1):
    yangneom = max(0, X-ban)
    fried = max(0, Y-ban)
    price = (ban * 2 * C) + (yangneom * A) + (fried * B)
    result = min(price, result)
print(result)