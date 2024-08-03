# 모듈 불러오기
from collections import deque

# 입력부
N, T, G = map(int, input().split())

# B 버튼 눌렀을 때 맨앞자리 1 제거하는 함수
def B(number):
    if number == 0: return 0 # 0일때 0출력
    if number > 99999: return 100000 # 이미 한계를 넘으면 넘은 값 출력

    # 자릿수 확인
    high = 0
    for tens in [1, 10, 100, 1000, 10000]:
        if number // tens: high = tens
    
    return number - high

# 초기값 선언
result = "ANG"
queue = deque([(N, 0)])
visited = [False for _ in range(100000)]
visited[N] = True

# BFS
while queue:
    value, count = queue.popleft()

    # 도착 여부 확인
    if value == G:
        result = count
        break

    # 다음 탐색
    for value_ in (value+1, B(value*2)):
        # 탐색 불가 조건
        if value_ > 99999: continue
        if count+1 > T: continue
        if visited[value_]: continue

        # 탐색
        visited[value_] = True

        # 다음 탐색
        queue.append((value_, count+1))

# 출력부
print(result)