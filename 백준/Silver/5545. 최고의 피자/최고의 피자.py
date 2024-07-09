# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
A, B = map(int, input().split())
C = int(input())
D = [int(input()) for _ in range(N)]

# 토핑 열량 정렬
D.sort(reverse=True)

# 현재 열량비 구하기
def getResult(energy, price): return int((energy/price) // 1)

# 초기값 선언
energy = C
price = A
result = getResult(energy, price)

# 열량 높은 토핑부터 넣어보기
for i in range(N):
    energy += D[i]
    price += B
    value = getResult(energy, price)

    # 열량비가 더 작아지면 나쁜 피자임
    if value < result: break 
    result = value

# 출력부
print(result)