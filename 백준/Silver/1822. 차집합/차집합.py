# 입력부
nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 출력부
result = sorted(list(A-B))
print(len(result))
if len(result): print(*result)