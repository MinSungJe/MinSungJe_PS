# 입력부
n, m = map(int, input().split())
if m != 0 : numbers = list(map(int, input().split()))

# 초기값 선언
visited = [0 for _ in range(10)]

# DFS
def DFS(idx):
    # 탐색 종료
    if idx == n:
        isPassword = True
        if m != 0:
            for number in numbers:
                if not visited[number] != 0: isPassword = False        
        return 1 if isPassword else 0
    
    # 다음 탐색
    result = 0
    for digit in range(10):
        visited[digit] += 1
        result += DFS(idx+1)
        visited[digit] -= 1
    
    return result

# 함수 호출 및 출력부
result = DFS(0)
print(result)