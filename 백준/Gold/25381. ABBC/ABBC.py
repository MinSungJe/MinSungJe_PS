# 입력부
S = input()
L = len(S)

# 초기값 선언
canDeleteCount = 0
BCount = 0
canDeleteBCount = 0
canDeleteACount = 0

# A-B 개수 확인
for i in range(L-1, -1, -1):
    if S[i] == 'B':
        canDeleteACount += 1
        BCount += 1
    if S[i] == 'A' and canDeleteACount > 0:
        canDeleteACount -= 1
        canDeleteCount += 1

# B-C 개수 확인
for i in range(L-1, -1, -1):
    if S[i] == 'C': canDeleteBCount += 1
    if S[i] == 'B' and canDeleteBCount > 0:
        canDeleteBCount -= 1
        canDeleteCount += 1

# 출력부
answer = min(canDeleteCount, BCount)
print(answer)