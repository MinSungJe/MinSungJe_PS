N = int(input())
answer = 0
while N > 1:
    if N % 2 == 1: N += 1
    else: N //= 2
    answer += 1
print(answer)