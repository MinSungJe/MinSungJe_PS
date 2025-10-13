# 입력부
N, K = map(int, input().split())
a_list = list(map(int, input().split()))

# 들어있는 숫자 개수 표시 리스트
a_number = [0 for _ in range(100001)]

# 투 포인터
l, r = 0, 0
answer = 0
for a in a_list:
    a_number[a] += 1
    while a_number[a] > K:
        a_number[a_list[l]] -= 1
        l += 1
    r += 1
    answer = max(r-l, answer)

# 출력부
print(answer)