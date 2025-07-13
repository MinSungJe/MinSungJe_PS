# 입력부
N = int(input())
fruits = list(map(int, input().split()))

# 초기값 선언
fruit_type = {fruits[0]: 1}
l = 0
r = 1

# 과일 종류가 2개 이하인지 확인
def is_available_fruit_type():
    answer = 0
    for value in fruit_type.values():
        if value > 0: answer += 1
    return answer <= 2

# 투 포인터
answer = 0
while True:
    if (l == r and r == N): break

    # 답 반영
    is_available = is_available_fruit_type()
    if is_available: answer = max(answer, r-l)

    # 과일 빼기
    if r == N or not is_available:
        fruit_type[fruits[l]] -= 1
        l += 1
        continue

    # 과일 추가
    if fruits[r] in fruit_type.keys(): fruit_type[fruits[r]] += 1
    else: fruit_type[fruits[r]] = 1
    r += 1

# 출력부
print(answer)