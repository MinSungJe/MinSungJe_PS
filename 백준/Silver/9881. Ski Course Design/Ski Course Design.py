# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
hills = [int(input()) for _ in range(N)]

# 최대 최소 구하기
min_hill, max_hill = min(hills), max(hills)

# 나올 수 있는 최대 최소별 결과 구하기
result = 10000001
for i in range(max_hill - 18):
    min_target = min_hill + i
    max_target = min_target + 17
    
    # 비용 구하기
    cost = 0
    for hill in hills:
        if hill < min_target: cost += (min_target - hill) ** 2
        if hill > max_target: cost += (hill - max_target) ** 2
    result = min(cost, result)
    
# 출력부
print(result)