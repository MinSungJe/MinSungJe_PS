# 입력부
N, Q = map(int, input().split())

# 초기값 선언
result = [0 for _ in range(N+1)]

# 풍선 꽂기
for _ in range(Q):
    L, I = map(int, input().split())
    for i in range(L, N+1, I):
        result[i] = 1

# 출력부
print(N-sum(result[1:]))