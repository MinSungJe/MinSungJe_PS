# 입력부
S, K = map(int, input().split())

# 몫과 나머지 구하기
value, rest = S//K, S%K

# 결과 구하기
result = 1
for _ in range(K-rest): result *= value
for _ in range(rest): result *= (value+1)

# 출력부
print(result)