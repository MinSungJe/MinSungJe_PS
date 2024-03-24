# 입력부
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

# DFS
def DFS(node, eggs):
    # 부술 계란 찾기
    result = 0
    for target_egg in range(N):
        # 탐색 불가 조건
        if node == target_egg: continue
        if eggs[target_egg][0] <= 0: continue

        # 계란으로 계란 치기
        eggs[node][0] -= eggs[target_egg][1]
        eggs[target_egg][0] -= eggs[node][1]

        # 깨진 계란 계산
        breakEgg = 0
        if eggs[node][0] <= 0: breakEgg += 1
        if eggs[target_egg][0] <= 0: breakEgg += 1
        result = max(result, breakEgg)

        # 다음 계란 찾기
        for node_ in range(node+1, N):
            # 탐색 불가 조건
            if eggs[node_][0] <= 0: continue

            result = max(result, breakEgg+DFS(node_, eggs))

        # backtracking
        eggs[node][0] += eggs[target_egg][1]
        eggs[target_egg][0] += eggs[node][1]

    return result

# 함수 호출
print(DFS(0, eggs))