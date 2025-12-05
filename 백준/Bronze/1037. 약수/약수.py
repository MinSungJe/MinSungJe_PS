# 입력부
N = int(input())
real_number = list(map(int, input().split()))

# 정렬
real_number.sort()

# 출력부
answer = real_number[0] * real_number[-1]
print(answer)