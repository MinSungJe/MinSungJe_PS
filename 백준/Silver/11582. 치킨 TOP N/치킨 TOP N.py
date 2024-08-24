# 입력부
N = int(input())
chicken = list(map(int, input().split()))
k = int(input())

# 정렬
result = list()
for i in range(0, N, N//k):
    result += sorted(chicken[i:i+N//k])

# 출력부
print(*result)