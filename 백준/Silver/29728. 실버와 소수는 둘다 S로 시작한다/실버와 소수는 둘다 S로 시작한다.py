# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())

# 소수 판독
MAX = 5000000
sosu = [True for _ in range(MAX+1)]
sosu[0], sosu[1] = False, False
for i in range(2, int(MAX ** (1/2)) + 1):
    if not sosu[i]: continue
    for j in range(2*i, MAX+1, i): sosu[j] = False

# 초기값 선언
reverse = False
A = deque()

# 문자열 만들기
for i in range(1, N+1):
    if not reverse:
        if not sosu[i]: A.append('B')
        else:
            A.pop()
            A.append('S')
            A.append('S')
            reverse = True
    else:
        if not sosu[i]: A.appendleft('B')
        else:
            A.popleft()
            A.appendleft('S')
            A.appendleft('S')
            reverse = False

# 결과 도출 및 출력부
Bcount, Scount = 0, 0
while A:
    value = A.pop()
    if value == 'B': Bcount += 1
    if value == 'S': Scount += 1
print(Bcount, Scount)