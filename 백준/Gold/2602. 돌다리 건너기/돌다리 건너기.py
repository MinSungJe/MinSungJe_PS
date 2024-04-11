# 입력부
turn = input()
demon = input()
angel = input()

# DP 배열 선언
DP = [[[-1, -1] for _ in range(len(demon))] for _ in range(len(turn))]

# DFS(+DP)
def DFS(idx, pos, isDemon):
    # 도착
    if idx >= len(turn): return 1
    # 탐색 실패
    if pos >= len(demon): return 0

    # 메모이제이션
    if DP[idx][pos][isDemon] != -1: return DP[idx][pos][isDemon]
    
    # 다음 탐색
    result = 0
    for i in range(pos, len(angel)):
        if isDemon:
            if demon[i] == turn[idx]: result += DFS(idx+1, i+1, 1-isDemon)
        else:
            if angel[i] == turn[idx]: result += DFS(idx+1, i+1, 1-isDemon)

    # 메모이제이션
    DP[idx][pos][isDemon] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 0, 1) + DFS(0, 0, 0)
print(result)