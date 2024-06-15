# 입력부
N = int(input())
target = list(map(int, input().split()))

# 초기값 선언
result = [-1]

# 뒤에서부터 오름차순이 아닌 수 확인
pre_number = 10001
for i in range(N-1, -1, -1):
    if target[i] < pre_number:
        pre_number = target[i]
        continue

    # 오름차순이 아닌 수 발견, 뒤에서 부터 그 수보다 작은 숫자랑 자리교환
    for j in range(N-1, i, -1):
        if target[j] > target[i]: continue
        temp = target[j]
        target[j] = target[i]
        target[i] = temp

        # 뒤 부분은 내림차순 정렬
        result = target[:i+1] + sorted(target[i+1:], reverse=True)
        break
    if result != [-1]: break

# 출력부
print(*result)