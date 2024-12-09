# 입력부
N, C = map(int, input().split())
numbers = list(map(int, input().split()))

# 기록하기
key_sequence = list()
number_dict = dict()
for i in range(N):
    key = numbers[i]
    if not key in number_dict.keys():
        key_sequence.append(key)
        number_dict[key] = 1
    else:
        number_dict[key] += 1

# 키배열 정렬
key_sequence.sort(key=lambda x:-number_dict[x])

# 결과 배열 만들기
result = list()
for key in key_sequence:
    for _ in range(number_dict[key]): result.append(key)

# 출력부
print(*result)