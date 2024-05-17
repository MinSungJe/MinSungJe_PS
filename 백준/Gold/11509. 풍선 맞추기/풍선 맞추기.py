# 입력부
N = int(input())
H = list(map(int, input().split()))

# 초기값 선언
arrow = dict()

# 필요한 화살 계산
for i in range(N):
    target = H[i]
    if arrow.get(target, 0) != 0: arrow[target] -= 1 # 화살 재사용 가능 
    if arrow.get(target-1, 0) != 0: arrow[target-1] += 1
    else: arrow[target-1] = 1

# 출력부
print(sum(arrow.values()))