# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, d, k, c = map(int, input().split())
rotate = list(int(input()) for _ in range(N))

# 결과값 도출
result = 0
for i in range(N):
    # 슬라이싱을 이용해 먹는 회전초밥 개수 구하기
    if i+k <= N:
        sushi = len(set(rotate[i:i+k]+[c]))
    else:
        sushi = len(set(rotate[i:N]+rotate[0:(i+k-N)]+[c]))
    result = max(result, sushi)

# 출력부
print(result)