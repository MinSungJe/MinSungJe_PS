# 빠른 입력 및 모듈 불러오기
from collections import defaultdict
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, d, k, c = map(int, input().split())
rotate = list(int(input()) for _ in range(N))

# 초기값 선언
sushi = defaultdict(int)
sushi[c] = 1
count = 1
for i in range(k):
    if not sushi[rotate[i]]: count += 1
    sushi[rotate[i]] += 1

# 결과값 도출
result = 0
for i in range(k, N+k):
    end = i%N # 마지막 포인터 위치
    
    # 새로운 초밥 하나 추가
    if not sushi[rotate[end]]: count += 1
    sushi[rotate[end]] += 1

    # 오래된 초밥 하나 삭제
    if sushi[rotate[end-k]] == 1: count -= 1
    sushi[rotate[end-k]] -= 1

    result = max(result, count)

# 출력부
print(result)