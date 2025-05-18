# 입력부
N = int(input())

# 제곱수 기록
answer = list()
for i in range(31): answer.append(2**i)

# 결과 도출 및 출력부
print(1 if N in answer else 0)