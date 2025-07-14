# 입력부
N = int(input())
S = list(map(int, input().split()))

# 초기값 선언
available_numbers = set()

# 비트 마스킹
for i in range(1 << N):
    result = 0
    for j in range(N):
        if i & 1 << j: result += S[j]
    available_numbers.add(result)

# 정렬
available_number_list = sorted(list(available_numbers))

# 결과 도출
answer = len(available_number_list)
for i in range(len(available_number_list)):
    if i == available_number_list[i]: continue
    answer = i
    break

# 출력부
print(answer)