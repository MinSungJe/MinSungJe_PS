# 입력부
N = int(input())

# 몫과 나머지 합하기
result = 0
for rest in range(1, N):
    result += rest*N + rest

# 출력부
print(result)