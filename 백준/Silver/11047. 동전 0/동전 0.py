# 입력부
N, K = map(int, input().split())
coins = []
for _ in range(N): coins.append(int(input()))

# 초기값 선언
result = 0

# 그리디 알고리즘 : 높은 값의 동전부터 사용
for coin in reversed(coins):
    result += K // coin
    K = K % coin

# 결과 출력
print(result)