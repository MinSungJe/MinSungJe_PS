# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
G = int(input())
P = int(input())

# 초기값 설정
Parking = [i for i in range(G+1)]
result = 0

# Union
def union(A, B):
    X = find(A)
    Y = find(B)
    if X == Y: return # 루트노드가 같음 : 이미 연결되어 있음
    Parking[Y] = X # 루트노드가 다름 : 한쪽 루트노드를 다른쪽 루트노드로 바꿈

# Find
def find(A):
    if Parking[A] == A: return A # 루트노드 발견
    Parking[A] = find(Parking[A]) # 경로 단축
    return Parking[A]


# 비행기가 들어올때마다 적절한지 확인(Find) 후 다음 비행기 행선지 옮기기(Union)
for _ in range(P):
    g = int(input())
    destination = find(g)
    if destination == 0:
        break
    union(destination-1, destination)
    result += 1

# 출력부
print(result)