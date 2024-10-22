# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
cards = dict()

# 카드 추가
for _ in range(N):
    card = int(input())
    if cards.get(card):
        cards[card] += 1
    else:
        cards[card] = 1

# 배열 돌며 가장 많은 카드 구하기
key_array = sorted(cards.keys())
result = key_array[0]
max_value = cards[key_array[0]]

for idx in key_array:
    value = cards[idx]
    if max_value < value:
        result = idx
        max_value = value

# 출력부
print(result)