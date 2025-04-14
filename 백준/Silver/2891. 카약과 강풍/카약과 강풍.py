# 입력부
N, S, R = map(int, input().split())
broken = list(map(int, input().split()))
spare = list(map(int, input().split()))

# 카약 현황 기록
boat = [[True, False] for _ in range(N+1)]
for idx in broken: boat[idx][0] = False
for idx in spare: boat[idx][1] = True

# 자체 스페어 배 사용하기
for i in range(1, N+1):
    if not boat[i][0] and boat[i][1]:
        boat[i][0] = True
        boat[i][1] = False

# 남은 스페어 배 사용하기
for i in range(1, N+1):
    if boat[i][1] == True:
        if not boat[i-1][0]:
            boat[i-1][0] = True
            boat[i][1] = False
            continue
        if i+1 <= N and not boat[i+1][0]:
            boat[i+1][0] = True
            boat[i][1] = False
            continue

# 결과 도출 및 출력부
result = 0
for i in range(1, N+1):
    if not boat[i][0]: result += 1
print(result)