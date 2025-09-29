# 입력부
N = int(input())
for i in range(1, N): print(' '*(N-i)+'*'*i)
print('*' * N)
for i in range(1, N): print(' '*i+'*'*(N-i))