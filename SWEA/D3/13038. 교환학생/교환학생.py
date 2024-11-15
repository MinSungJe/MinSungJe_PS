TC = int(input())
for test_case in range(1, TC+1):
    n = int(input())
    days = list(map(int, input().split()))
    
    result = 700001
    for day in range(7):
        count = 0
        classCount = 0
        while classCount < n:
            count += 1
            if days[day]: classCount += 1
            day = (day+1) % 7
        result = min(result, count)
    
    print(f"#{test_case} {result}")