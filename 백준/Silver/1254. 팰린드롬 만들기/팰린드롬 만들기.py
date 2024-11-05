# 입력부
S = input()

# 초기값 선언
L = len(S)
result = 0

# 가능한 길이마다 확인
for length in range(len(S), 101):
    canPalin = True
    for i in range(length//2):
        match_idx = (length-1)-i
        if match_idx >= L: continue
        if S[i] != S[match_idx]:
            canPalin = False
            break
    if canPalin:
        result = length
        break

# 출력부
print(result)