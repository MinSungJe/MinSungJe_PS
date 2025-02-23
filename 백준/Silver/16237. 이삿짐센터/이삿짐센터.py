# 입력부
A, B, C, D, E = map(int, input().split())

# 크기가 큰 물건부터 담기
result = 0
# 크기가 5: 그냥 담기
while E:
    E -= 1
    result += 1

# 크기가 4: 크기가 1인 물건이랑 함께 담기
while D:
    D -= 1
    if A: A -= 1
    result += 1

# 크기가 3: 크기가 2인 물건이랑 함께 담고 없다면 1인 물건 두 개씩 담기
while C:
    C -= 1
    if B: B -= 1
    elif A: A -= min(2, A)
    result += 1

# 크기가 2: 크기가 2인 물건이랑 담고 크기가 1인 물건이랑 최대한 담기
while B:
    storage = 5
    B_value = min(B, 2)
    storage -= 2 * B_value
    B -= B_value
    if A: A -= min(storage, A)
    result += 1

# 크기가 1: 최대한 겹쳐 담기
while A:
    A_value = min(A, 5)
    A -= A_value
    result += 1

# 출력부
print(result)