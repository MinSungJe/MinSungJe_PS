# 입력부
N = int(input())
V = list(map(int, input().split()))

# 결과값 계산
result = 0
speed = 0

# 결과값 계산
for i in range(N-1, -1, -1):
    if speed >= V[i]:
        speed = V[i]
    else:
        speed = min(speed+1, V[i])

    # 속도 반영
    result += speed

# 출력부
print(result)