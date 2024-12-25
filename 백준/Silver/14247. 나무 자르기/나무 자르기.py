# 입력부
n = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

# 나무 자르기
result = sum(H)
A.sort()
for i in range(n): result += A[i] * i

# 출력부
print(result)