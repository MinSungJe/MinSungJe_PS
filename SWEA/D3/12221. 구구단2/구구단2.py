TC = int(input())
for test_case in range(1, TC+1):
    A, B = map(int, input().split())
    result = True
    if A >= 10: result = False
    if B >= 10: result = False
        
    print(f"#{test_case} {A*B if result else -1}")