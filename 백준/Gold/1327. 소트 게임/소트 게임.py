# 모듈 불러오기
from collections import deque

# 입력부
N, K = map(int, input().split())
numbers = ''.join(input().split())

# 뒤집기 함수
def flip(numbers, idx):
    return numbers[:idx] + get_reversed_string(numbers[idx:idx+K]) + numbers[idx+K:]

def get_reversed_string(letter):
    result = ''
    for l in letter: result = l + result 
    return result

# 오름차순 확인 함수
def check_is_asc(numbers):
    prev_value = 0
    for number in numbers:
        value = int(number)
        if prev_value > value: return False
        prev_value = value
    return True

# 초기값 선언
queue = deque([(numbers, 0)])
visited = set()


# BFS
result = -1
while queue:
    node, count = queue.popleft()

    # 탐색 불가 조건
    if node in visited: continue

    # 탐색
    if check_is_asc(node):
        result = count
        break
    visited.add(node)

    # 다음 탐색
    for idx in range(0, N-K+1):
        node_ = flip(node, idx)
        queue.append((node_, count+1))

# 출력부
print(result)