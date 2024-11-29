# 입력부
N = int(input())
count = int(input())
recommends = list(map(int, input().split()))

# 초기값 선언
score = [0 for _ in range(101)]
score[0] = 1001
result = list()

# 추천 받기
for recommend in recommends:
    if recommend in result:
        score[recommend] += 1
        continue

    if len(result) < N:
        result.append(recommend)
        score[recommend] += 1
        continue

    min_value = 0
    for value in result:
        if score[value] >= score[min_value]: continue
        min_value = value
    result.remove(min_value)
    score[min_value] = 0
    result.append(recommend)
    score[recommend] += 1
        
# 출력부
result.sort()
print(*result)