# 입력부
N = int(input())

# 먹은 횟수 저장
count = dict()

# 먹은 횟수 확인하며 음식 먹이기
result = 0
for _ in range(N):
    name = input()

    # 다른 사람이 먹은 횟수의 합
    sum_value = 0
    for k, v in count.items():
        if k == name: continue
        sum_value += v

    # 자신이 먹은 횟수 확인
    if not name in count.keys(): value = 0
    else: value = count[name]

    # 횟수 비교 후 훈육 여부 확인
    if value > sum_value: result += 1

    # 횟수 추가
    if not name in count.keys(): count[name] = 1
    else: count[name] += 1

# 출력부
print(result)