TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []
    
    for _ in range(N):
        max_value = numbers[-1]
        discount_value = int(max_value * 0.75)
        result.append(discount_value)
        numbers.remove(max_value)
        numbers.remove(discount_value)
    
    result.sort()
    print(f"#{test_case} {' '.join(map(str, result))}")