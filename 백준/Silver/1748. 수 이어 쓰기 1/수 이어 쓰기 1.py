# 입력부
N = int(input())

# 초기값 선언
answer = 0
numbers = 1
startNumber = 1

while startNumber * 10 <= N:
    answer += (startNumber * 10 - startNumber) * numbers
    startNumber *= 10
    numbers += 1

# 남은 구간 추가
answer += (N - startNumber + 1) * numbers

# 출력부
print(answer)