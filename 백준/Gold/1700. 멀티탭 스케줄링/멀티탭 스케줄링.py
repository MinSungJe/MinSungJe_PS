# 입력부
N, K = map(int, input().split())
turn = list(map(int, input().split()))

# 초기값 선언
plugged = list()
result = 0

# 멀티탭 꽂기
for i in range(K):
    number = turn[i]
    if number in plugged: continue
    if len(plugged) < N:
        plugged.append(number)
        continue

    late_idx, late_value = i, plugged[0]
    for value in plugged:
        # 뒤에 아예 쓸일 없는 경우부터 확인
        if not value in turn[i:]:
            late_value = value
            break

        # 가장 늦게 나오는 전기용품 찾기
        for idx in range(i, K):
            if turn[idx] != value: continue
            if late_idx < idx:
                late_idx = idx
                late_value = value            
            break
    
    # 전기용품 플러그 교체
    plugged.remove(late_value)
    plugged.append(number)
    result += 1

# 출력부
print(result)