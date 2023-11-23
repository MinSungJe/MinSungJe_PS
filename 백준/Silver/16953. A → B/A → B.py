# 입력부
A, B = map(int, input().split())

# 초기값 선언
temp = B
count = 1
result = -1

# B -> A로 이동
while temp >= A:
    if temp == A:
        result = count
        break

    if temp % 2 == 0: temp = temp//2 # 짝수인 경우 전 단계에서 2를 곱한 것
    else:
        if temp % 10 == 1: temp = temp // 10 # 1의 자리가 1이면 오른쪽에 1을 더한 것
        else: break # 1의 자리가 1이 아닌 홀수는 불가능

    count += 1

# 출력부
print(result)