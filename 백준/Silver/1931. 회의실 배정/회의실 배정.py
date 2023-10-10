# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
meeting = []
for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

# 그리디 알고리즘을 위한 정렬 : 끝나는 시간으로 정렬
meeting.sort(key=lambda x:(x[1],x[0]))

# 초기값 설정
time = 0
result = 0

# 그리디 알고리즘 : 뒤에서부터 탐색
for t in meeting:
    if t[0] >= time:
        time = t[1]
        result += 1

# 결과 출력
print(result)