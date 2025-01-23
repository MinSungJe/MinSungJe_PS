# 입력부
n = int(input())
result = 0
status = 0

# 요금 확인
for _ in range(n):
    t = int(input())
    status += t
    result = min(result, status)

# 출력부
print(abs(result))