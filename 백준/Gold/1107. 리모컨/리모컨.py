# 입력부
N = int(input())
M = int(input())
if M: btn = set(input().split())
else: btn = set()

# 초기 값 선언
Max = 1000000
upper = [Max,-1]
lower = [Max,-1]

# 자릿수 찾는 함수
def number(num):
    return len(str(num))

# 조건에 맞는 가장 가까운 채널과 버튼 누른 횟수 찾기
# 채널을 높여보자
for i in range(N,Max):
    upper[1] += 1
    if not set(str(i)).intersection(btn):
        upper[0] = i
        upper[1] += number(i)
        break
    if i == Max: upper[1] = Max

# 채널을 낮춰보자
for i in range(N,-1,-1):
    lower[1] += 1
    if not set(str(i)).intersection(btn):
        lower[0] = i
        lower[1] += number(i)
        break
    if i == 0: lower[1] = Max

# 출력부
print(min(upper[1], lower[1], abs(N-100)))