S = input()
T = input()
LCS = [[0 for _ in range(len(T)+1)] for _ in range(len(S)+1)]

for i in range(1,len(S)+1):
	for j in range(1,len(T)+1):
		if S[i-1] == T[j-1]:
			LCS[i][j] = LCS[i-1][j-1] + 1
		else:
			LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
			
print(LCS[len(S)][len(T)])