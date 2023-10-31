# 입력부
N, M = map(int, input().split())
know = set(list(map(int, input().split()))[1:])
party = []
for _ in range(M):
    party.append(set(list(map(int, input().split()))[1:]))

# 초기값 선언
result = 0

# M번 반복
for _ in range(M):
    # 진실을 알 수 밖에 없는 인원 재정립
    for p in party:
        if set.intersection(know, p):
            know = set.union(know, p)

# 진실을 알고 있는 사람이 없는 파티만큼 과장 가능
for p in party:
    if not set.intersection(know, p):
        result += 1

# 출력부
print(result)