T = int(input())
for test_case in range(1, T+1):
    first, second, third = map(int, input().split())
    
    result = 0
    if second >= third:
        result += second - (third-1)
        second = third-1
    if first >= second:
        result += first - (second-1)
        first = second-1
        
    if first <= 0: result = -1
    print(f"#{test_case} {result}")