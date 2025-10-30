# 입력부
S = input()
L = len(S)

# 초기값 선언
answer = 0
isUsedB = [False for _ in range(L)]
canDeleteBCount = 0
canDeleteACount = 0

# B-C 확인
for i in range(L-1, -1, -1):
    if S[i] == 'C':
        canDeleteBCount += 1
    if S[i] == 'B' and canDeleteBCount > 0:
        isUsedB[i] = True
        canDeleteBCount -= 1
        answer += 1

# A-B 확인
for i in range(L-1, -1, -1):
    if S[i] == 'B' and not isUsedB[i]:
        canDeleteACount += 1
    if S[i] == 'A' and canDeleteACount > 0:
        canDeleteACount -= 1
        answer += 1

# 출력부
print(answer)