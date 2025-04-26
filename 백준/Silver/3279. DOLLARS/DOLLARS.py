# 입력부
N = int(input())
A = [int(input()) for _ in range(N)]

# 초기값 선언
idx = 0
result = 100
dollar = 100
marks = 0
current = 0

# 달러-마르크 거래
while True:
    # 거래 종료
    if idx == N:
        dollar = (marks / current) * 100
        result = max(result, dollar)
        break

    # 그리디 알고리즘
    value = A[idx]

    # 마르크 가장 많이 사기
    if dollar:
        if current <= value:
            current = value
            idx += 1
        else:
            marks = (dollar / 100) * current
            dollar = 0
    
    # 달러 가장 많이 사기
    else:
        if current >= value:
            current = value
            idx += 1
        else:
            dollar = (marks / current) * 100
            result = max(result, dollar) # 달러 최대치 기록
            marks = 0

# 출력부
print(f"{result:.2f}")