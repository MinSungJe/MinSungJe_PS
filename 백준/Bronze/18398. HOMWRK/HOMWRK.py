T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        print(A+B, A*B)