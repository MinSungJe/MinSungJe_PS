# 입력부
N = int(input())
num = list(map(int, input().split()))

# 절댓값으로 정렬
num.sort(key=lambda x:abs(x))

# O(N) 탐색
temp = 20000000001
result = [0, 0]
for i in range(N-1):
    if abs(num[i] + num[i+1]) < temp:
        temp = abs(num[i] + num[i+1])
        result[0] = num[i]
        result[1] = num[i+1]

# 출력부
print(*sorted(result))