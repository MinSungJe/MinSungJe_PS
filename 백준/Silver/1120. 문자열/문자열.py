# 입력부
A, B = input().split()

# 차이 비교
result = 51
for start in range(len(B)-len(A)+1):
    value = 0
    for i in range(len(A)):
        if A[i] != B[start+i]: value += 1

    result = min(result, value)

# 출력부
print(result)