# 입력부
N, D = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]

# DFS 완전탐색
def DFS(pos):
    # 다음 탐색
    result = 120001
    for start, end, value in road:
        if start < pos or end > D: continue # 이미 지나침
        result = min(result, (start-pos)+value+DFS(end))
    result = min(result, D-pos)
    return result

# 함수 호출 및 출력부
result = DFS(0)
print(result)