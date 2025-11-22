# 입력부
L, R, B = map(int, input().split())

# 양발잡이 분배
answer = 0
for i in range(B+1):
    answer = max(answer, min(L+i, R+(B-i)) * 2)

# 출력부 
print(answer)