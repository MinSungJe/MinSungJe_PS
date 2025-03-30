# 입력부
N = int(input())
jewel = input()

# 반복문을 돌며 확인
result = 1
value = 1
for i in range(N-1):
    if (jewel[i] == "R" and jewel[i+1] == "B") or (jewel[i] == "B" and jewel[i+1] == "R"):
        value += 1
        result = max(result, value)
        continue
    value = 1

# 출력부
print(result)