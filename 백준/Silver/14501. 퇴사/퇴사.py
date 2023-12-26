# 입력부
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
DP = [0 for _ in range(N)]

# DP(Top-Down)
def DFS(day):
    if day == N: return 0 # 탐색 불가 조건
    if DP[day]: return DP[day]

    # 탐색
    if day+table[day][0] > N:
        result = DFS(day+1)
    else:
        result = max(table[day][1]+DFS(day+table[day][0]), DFS(day+1))
    DP[day] = result
    return result

# 함수 호출 및 출력부
result = DFS(0)
print(result)