# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
S = input()
N = int(input())
A = list(input() for _ in range(N))

# DP 배열 선언
DP = [0 for _ in range(len(S)+1)]
DP[0] = 1

# DP 배열 채우기
for i in range(len(S)+1):
    for j in range(N):
        word = A[j]
        
        # 추가 불가 조건
        if i+len(word) > len(S): continue
        if S[i:i+len(word)] != word: continue
            
        # 채우기
        DP[i+len(word)] += DP[i]

# 출력부
print(1 if DP[-1] else 0)