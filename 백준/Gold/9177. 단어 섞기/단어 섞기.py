# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
T = int(input())
for test_case in range(1, T+1):
    words = list(input().split())

    # 초기값 선언
    result = False
    first_word = list(words[0])
    second_word = list(words[1])
    target = list(words[2])
    N = len(target)
    first_len = len(first_word)
    second_len = len(second_word)

    # BFS 요소 선언
    queue = deque([(0, 0, 0)])
    visited = [[False for _ in range(second_len+1)] for _ in range(first_len+1)]
    visited[0][0] = True

    # BFS
    while queue:
        idx, first_idx, second_idx = queue.popleft()

        # 단어 완성
        if idx >= N:
            result = True
            break

        # 다음 탐색
        if first_idx < first_len and first_word[first_idx] == target[idx] and not visited[first_idx+1][second_idx]:
            # 탐색
            visited[first_idx+1][second_idx] = True
            queue.append((idx+1, first_idx+1, second_idx))
        if second_idx < second_len and second_word[second_idx] == target[idx] and not visited[first_idx][second_idx+1]:
            # 탐색
            visited[first_idx][second_idx+1] = True
            queue.append((idx+1, first_idx, second_idx+1))

    # 출력부
    print(f"Data set {test_case}: yes" if result else f"Data set {test_case}: no")