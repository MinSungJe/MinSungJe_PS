# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
T = int(input())
for _ in range(T):
    letter = input()

    # 초기값 선언
    result = 2
    queue = deque([(0, len(letter)-1, 0)])

    # queue에 투 포인터 값 넣어가며 확인
    while queue:
        left, right, count = queue.popleft()

        # 탐색 불가 조건
        if count >= 2: continue

        # 탐색 완료
        if left > right:
            result = min(count, result)
            continue

        # 다음 탐색
        if letter[left] == letter[right]: queue.append((left+1, right-1, count))
        if letter[left+1] == letter[right]: queue.append((left+2, right-1, count+1))
        if letter[left] == letter[right-1]: queue.append((left+1, right-2, count+1))

    # 출력부
    print(result)