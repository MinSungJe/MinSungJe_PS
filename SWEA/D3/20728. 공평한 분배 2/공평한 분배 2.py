T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))
    
    result = 1000000001
    candy.sort()
    for i in range(N-(K-1)):
        result = min(result, candy[i+(K-1)] - candy[i])
    
    print(f"#{test_case} {result}")