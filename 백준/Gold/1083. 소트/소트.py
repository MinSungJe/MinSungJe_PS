# 입력부
N = int(input())
numbers = list(map(int, input().split()))
S = int(input())

# S 값에 따라 확인
for idx in range(N):
    max_idx = idx
    max_value = numbers[idx]

    # S 범위 내에서 확인
    for i in range(1, S+1):
        idx_ = idx+i
        if idx_ >= N: break
        if numbers[idx_] > numbers[max_idx]:
            max_idx = idx_
            max_value = numbers[idx_]
    
    # 교환
    for i in range(max_idx, idx, -1):
        numbers[i] = numbers[i-1]
    numbers[idx] = max_value

    # S 값 반영
    S -= max_idx - idx

# 출력부
print(*numbers)