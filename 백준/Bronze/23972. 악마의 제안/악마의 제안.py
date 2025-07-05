K, N = map(int, input().split())
if N == 1: print(-1)
else:
    answer = N * K // (N - 1)
    if N*K % (N-1): answer += 1
    print(answer)