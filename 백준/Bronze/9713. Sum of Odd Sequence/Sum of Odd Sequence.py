T = int(input())
for _ in range(T):
    N = int(input())
    answer = 0
    for i in range(1, N+1, 2): answer += i
    print(answer)