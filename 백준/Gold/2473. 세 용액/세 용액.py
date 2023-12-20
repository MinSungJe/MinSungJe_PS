# 입력부
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

# 초기값 선언
result = [0,0,0]
best_value = 3000000001

# 첫 번째 용액 선택(N)
for k in range(N):
    i = 0
    j = N-1

    # 투포인터(N)
    while i < j:
        # 겹치는 경우 탐색 X
        if i == k:
            i += 1
            continue
        if j == k:
            j -= 1
            continue
        
        # 갱신
        value = numbers[i] + numbers[j] + numbers[k]
        if abs(value) < best_value:
            result[0] = numbers[i]
            result[1] = numbers[j]
            result[2] = numbers[k]
            best_value = abs(value)

        if value < 0:
            i += 1
        if value > 0:
            j -= 1
        if value == 0: break
    
    if value == 0: break
    
# 출력부
print(*sorted(result))