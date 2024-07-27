# 모듈 불러오기
from itertools import permutations

# 입력부
n = int(input())
k = int(input())
card = [input() for _ in range(n)]

# 카드 조합
result = list()
for c in permutations(card, k):
    value = ''.join(c)
    result.append(value)

# 출력부
print(len(set(result)))