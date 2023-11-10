# 입력부
N, M = map(int, input().split())
numbers = list(input().split())

# 초기값 선언
visited = [False for _ in range(N)]
temp = []
result = []

# DFS
def DFS(count):
    global visited, temp
    prev = temp[:]
    if count == M:
        result.append(' '.join(temp))
        return
    
    # 재귀 호출
    for i in range(N):
        if visited[i]: continue
        temp.append(numbers[i])
        visited[i] = True
        DFS(count + 1)
        temp = prev[:]
        visited[i] = False

# 함수 호출 및 출력부
DFS(0)
result = list(set(result))
for i in range(len(result)):
    result[i] = list(map(int,result[i].split(' ')))
result.sort()

for ans in result:
    print(*ans)