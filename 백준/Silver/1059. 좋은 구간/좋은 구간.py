# 입력부
L = int(input())
S = list(map(int, input().split()))
n = int(input())

# 집합 정렬
S += [0]
S.sort()

# 어느 구간에 속하는지 확인
idx = -1
for i in range(L+1):
    if n > S[i]: idx = i
    if n == S[i]:
        print(0)
        exit()

# 결과값 도출
result, left, right = 0, 0, 0
left = n-S[idx]-1 # n보다 작은 숫자의 개수
right = S[idx+1]-n # n보다 크거나 같은 숫자의 개수
result = left * right + (right-1)

# 출력부
print(result)