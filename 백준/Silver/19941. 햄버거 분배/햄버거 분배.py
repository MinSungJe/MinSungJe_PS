# 입력부
N, K = map(int, input().split())
letter = input()

# 초기값 선언
visited = [False for _ in range(N)]

# 사람마다 햄버거 매칭
result = 0
for i in range(N):
    if letter[i] == 'P':
        min_idx = max(0, i-K)
        max_idx = min(N, i+K+1)
        for j in range(min_idx, max_idx):
            if letter[j] == 'H' and not visited[j]:
                visited[j] = True
                result += 1
                break

# 출력부
print(result)